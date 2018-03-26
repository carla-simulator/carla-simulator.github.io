# https://gist.github.com/joelverhagen/1805814
class YouTube < Liquid::Tag
  Syntax = /^\s*([^\s]+)(\s+(\d+)\s+(\d+)\s*)?/

  def initialize(tagName, markup, tokens)
    super

    if markup =~ Syntax then
      @id = $1
    else
      raise "No YouTube ID provided in the \"youtube\" tag"
    end
  end

  def render(context)
    "<div class=\"intrinsic-container intrinsic-container-16x9\"><iframe src=\"https://www.youtube.com/embed/#{@id}?feature=oembed\" frameborder=\"0\" gesture=\"media\" allowfullscreen=\"\" class=\"fluidvids-item\" data-fluidvids=\"loaded\"></iframe></div>"
  end

  Liquid::Template.register_tag "youtube", self
end
