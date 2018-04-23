#!/usr/bin/env python2

# Copyright (c) 2017 Computer Vision Center (CVC) at the Universitat Autonoma de
# Barcelona (UAB).
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

"""Passes some unit tests on our posts."""


import datetime
import inspect
import os
import re
import sys
import yaml


def print_out(message, *args):
    print(message % args)


class File(object):
    def __init__(self, filepath):
        self.filepath = filepath
        self.date = None
        self.metadata = {}

    def parse(self):
        with open(self.filepath) as fp:
            for x in yaml.load_all(fp):
                self.metadata = x
                break

    def parse_date(self):
        date_format = '%Y-%m-%d %H:%M:%S +0002'
        self.date = datetime.datetime.strptime(self.metadata['date'], date_format)

    def test_fields(self, fields):
        missing = [f for f in fields if f not in self.metadata]
        if not missing:
            return True, None
        elif len(missing) == 1:
            return False, ('Missing field %r' % missing[0])
        else:
            missing_str = ', '.join(['%r' % x for x in missing])
            return False, ('Missing fields %s' % missing_str)


class FileTester(object):
    __priority__ = 100
    def test(self, _):
        raise NotImplementedError


# ==============================================================================
# -- Testers -------------------------------------------------------------------
# ==============================================================================


class ParseHeader(FileTester):
    __priority__ = 0
    def test(self, file_obj):
        try:
            file_obj.parse()
        except Exception as exception:
            return False, str(exception)
        return file_obj.test_fields(['layout', 'title', 'date', 'author', 'comments'])


class Title(FileTester):
    __priority__ = 1
    def __init__(self):
        self.titles = []

    def test(self, file_obj):
        title = file_obj.metadata['title']

        if len(title) < 8:
            return False, 'Title is too short (at least 8 chars required)'

        if title in self.titles:
            return False, 'Another post already has this title'
        self.titles.append(title)

        return True, None


class DateTime(FileTester):
    __priority__ = 1
    def test(self, file_obj):
        try:
            file_obj.parse_date()

            if file_obj.date > datetime.datetime.now():
                return False, 'Future date-time'

        except Exception as exception:
            return False, str(exception)
        return True, None


class FileName(FileTester):
    __priority__ = 2
    def __init__(self):
        self.format = '_posts/YYYY-MM-DD-title.md'
        self.regex = re.compile(r'^_posts/(\d{4}-\d{2}-\d{2})-(.*)\.md$')
        self.format_release = '_posts/YYYY-MM-DD-release-X.X.X.md'
        self.regex_release = re.compile(r'^release-\d+\.\d+\.\d+$')

    def test(self, file_obj):
        match = self.regex.match(file_obj.filepath)

        if match is None:
            error_message = 'Invalid filename: file names should follow the format %r'
            return False, (error_message % self.format)

        date, title = match.groups()

        if len(title) < 8:
            return False, 'Title is too short (at least 8 chars required)'

        if 'release' in title:
            if self.regex_release.match(title) is None:
                error_message = 'Invalid "release" post: should follow the format %r'
                return False, (error_message % self.format_release)

        try:

            date = datetime.datetime.strptime(date, '%Y-%m-%d')

            if file_obj.date is not None and date.date() != file_obj.date.date():
                return False, 'Date-time missmatch'

            if date > datetime.datetime.now():
                return False, 'Future date-time'

        except Exception as exception:
            return False, ('Invalid date: %s' % exception)
        return True, None


class Author(FileTester):
    def test(self, file_obj):
        try:
            authors = file_obj.metadata['author'].split(' ')

            for author in authors:
                if author != 'and' and not author.startswith('@'):
                    return False, ('Invalid username %r (must be a @mention)' % author)

        except Exception as exception:
            return False, ('Invalid author: %s' % exception)
        return True, None


class SEO(FileTester):
    def test(self, file_obj):
        res = file_obj.test_fields(['description', 'image'])
        if not res[0]:
            return res

        if len(file_obj.metadata['description']) < 30:
            return False, 'Description is too short (at least 30 chars required)'

        return True, None


# ==============================================================================
# -- Main script ---------------------------------------------------------------
# ==============================================================================


def iterate_tester_classes():
    for _, obj in inspect.getmembers(sys.modules[__name__]):
        if obj != FileTester and inspect.isclass(obj) and issubclass(obj, FileTester):
            yield obj


def iterate_posts():
    for dirpath, _, filenames in os.walk('_posts'):
        for filename in filenames:
            yield os.path.join(dirpath, filename)


def check_posts():
    tester_classes = [x for x in iterate_tester_classes()]
    testers = [x() for x in sorted(tester_classes, key=lambda x: x.__priority__)]

    files = sorted([File(x) for x in iterate_posts()], key=lambda x: x.filepath)

    print_out('Running %d tests on %d posts...', len(testers), len(files))

    fail_count = 0

    for file_obj in files:
        print_out('\n%s', file_obj.filepath)
        for tester in testers:
            result, message = tester.test(file_obj)
            fail_count += 0 if result else 1
            print_out(
                '  - %s    %s%s',
                'OK    ' if result else 'FAILED',
                type(tester).__name__,
                '' if not message else ': ' + message)

    if fail_count > 0:
        print_out('\n%d tests failed!\n', fail_count)
    else:
        print_out('\nSUCCESS!\n')

    return fail_count


if __name__ == '__main__':

    sys.exit(check_posts())
