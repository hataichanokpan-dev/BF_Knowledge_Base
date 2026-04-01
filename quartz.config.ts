import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

/**
 * Quartz 4 Configuration
 *
 * See https://quartz.jzhao.xyz/configuration for more information.
 */
const config: QuartzConfig = {
  configuration: {
    pageTitle: "BF Knowledge Base",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "en-US",
    baseUrl: "bf-knowledge-base.vercel.app",
    ignorePatterns: ["private", "templates", ".obsidian", ".trash", ".base"],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Playfair Display",
        body: "Lora",
        code: "JetBrains Mono",
      },
      colors: {
        lightMode: {
          light: "#fdfbf7",       // warm paper
          lightgray: "#e8e4dc",
          gray: "#9a9a9a",
          darkgray: "#5a5a5a",
          dark: "#3d3d3d",        // softer than pure black
          secondary: "#8b4513",   // saddle brown (book spine)
          tertiary: "#a0522d",    // sienna
          highlight: "rgba(139, 69, 19, 0.08)",
          textHighlight: "rgba(139, 69, 19, 0.25)",
        },
        darkMode: {
          light: "#1a1a1f",       // soft black
          lightgray: "#2a2a30",
          gray: "#6a6a70",
          darkgray: "#c8c4bc",    // warm white
          dark: "#e8e4dc",        // warm paper white
          secondary: "#cd853f",   // peru (warm accent)
          tertiary: "#d2691e",    // chocolate
          highlight: "rgba(205, 133, 63, 0.12)",
          textHighlight: "rgba(205, 133, 63, 0.3)",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
        rssSlug: "rss", // Changed from default "index" to avoid conflict with index.html
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      // Comment out CustomOgImages to speed up build time
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
