# Gemfile for GitHub Pages

source "https://rubygems.org"

# Jekyll 版本
gem "jekyll", "~> 3.9.0"

# GitHub Pages gem - 包含所有 GitHub Pages 支持的插件
gem "github-pages", group: :jekyll_plugins

# 其他有用的插件
group :jekyll_plugins do
  gem "jekyll-feed", "~> 0.12"
  gem "jekyll-sitemap"
  gem "jekyll-seo-tag"
  gem "jekyll-relative-links"
end

# Windows 和 JRuby 不包含 zoneinfo 文件，需要使用 tzinfo-data gem
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", "~> 1.2"
  gem "tzinfo-data"
end

# Windows 性能增强
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]