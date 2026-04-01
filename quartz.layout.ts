import { PageLayout, SharedLayout } from "./quartz/cfg"
import * as Component from "./quartz/components"
import ReadingProgress from "./quartz/components/ReadingProgress"
import ReadingTime from "./quartz/components/ReadingTime"
import RelatedNotes from "./quartz/components/RelatedNotes"

// components shared across all pages
export const sharedPageComponents: SharedLayout = {
  head: Component.Head(),
  header: [ReadingProgress()],
  afterBody: [],
  footer: Component.Footer({
    links: {
      GitHub: "https://github.com/jackyzha0/quartz",
      "Discord Community": "https://discord.gg/cRFFHYye7t",
    },
  }),
}

// components for pages that display a single page (e.g. a single note)
export const defaultContentPageLayout: PageLayout = {
  beforeBody: [
    Component.ConditionalRender({
      component: Component.Breadcrumbs(),
      condition: (page) => page.fileData.slug !== "index",
    }),
    Component.ArticleTitle(),
    ReadingTime(), // Show reading time
    Component.ContentMeta(),
    Component.TagList(),
  ],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
        { Component: Component.ReaderMode() },
      ],
    }),
    Component.Explorer(),
    // DesktopOnly: RecentNotes hidden on mobile to save space
    Component.DesktopOnly(
      Component.RecentNotes({
        title: "📖 บทความล่าสุด",
        limit: 5,
        showTags: true,
      }),
    ),
  ],
  right: [
    Component.Graph(),
    Component.DesktopOnly(Component.TableOfContents()),
    Component.Backlinks(),
    // DesktopOnly: RelatedNotes hidden on mobile
    Component.DesktopOnly(
      RelatedNotes({
        title: "🔗 บทความที่เกี่ยวข้อง",
        limit: 5,
        minTagOverlap: 1,
      }),
    ),
  ],
}

// components for pages that display lists of pages  (e.g. tags or folders)
export const defaultListPageLayout: PageLayout = {
  beforeBody: [Component.Breadcrumbs(), Component.ArticleTitle(), Component.ContentMeta()],
  left: [
    Component.PageTitle(),
    Component.MobileOnly(Component.Spacer()),
    Component.Flex({
      components: [
        {
          Component: Component.Search(),
          grow: true,
        },
        { Component: Component.Darkmode() },
      ],
    }),
    Component.Explorer(),
    Component.DesktopOnly(
      Component.RecentNotes({
        title: "📖 บทความล่าสุด",
        limit: 5,
        showTags: true,
      }),
    ),
  ],
  right: [],
}
