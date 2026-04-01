import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { resolveRelative, FullSlug, SimpleSlug } from "../util/path"
import { QuartzPluginData } from "../plugins/vfile"
import { i18n } from "../i18n"
import { classNames } from "../util/lang"
import style from "./styles/recentNotes.scss"

interface Options {
  title?: string
  limit: number
  minTagOverlap: number
  filter: (f: QuartzPluginData) => boolean
}

const defaultOptions: Options = {
  limit: 5,
  minTagOverlap: 1,
  filter: () => true,
}

// Calculate tag overlap between two notes
function tagOverlap(tags1: string[], tags2: string[]): number {
  const set1 = new Set(tags1)
  const set2 = new Set(tags2)
  let count = 0
  for (const tag of set1) {
    if (set2.has(tag)) count++
  }
  return count
}

export default ((userOpts?: Partial<Options>) => {
  const opts = { ...defaultOptions, ...userOpts }

  const RelatedNotes: QuartzComponent = ({
    allFiles,
    fileData,
    displayClass,
    cfg,
  }: QuartzComponentProps) => {
    // Get current note's tags
    const currentTags = fileData.frontmatter?.tags ?? []
    const currentSlug = fileData.slug

    if (currentTags.length === 0) return null

    // Filter and sort by tag overlap
    const relatedFiles = allFiles
      .filter((f) => {
        // Exclude current file
        if (f.slug === currentSlug) return false
        // Exclude if no tags
        const fTags = f.frontmatter?.tags ?? []
        if (fTags.length === 0) return false
        // Apply custom filter
        if (!opts.filter(f)) return false
        // Check minimum overlap
        return tagOverlap(currentTags, fTags) >= opts.minTagOverlap
      })
      .map((f) => ({
        file: f,
        overlap: tagOverlap(currentTags, f.frontmatter?.tags ?? []),
      }))
      .sort((a, b) => b.overlap - a.overlap)
      .slice(0, opts.limit)

    if (relatedFiles.length === 0) return null

    return (
      <div class={classNames(displayClass, "related-notes")}>
        <h3>{opts.title ?? "🔗 บทความที่เกี่ยวข้อง"}</h3>
        <ul class="related-ul">
          {relatedFiles.map(({ file, overlap }) => {
            const title = file.frontmatter?.title ?? i18n(cfg.locale).propertyDefaults.title
            const tags = file.frontmatter?.tags ?? []

            return (
              <li class="related-li">
                <div class="section">
                  <div class="desc">
                    <a href={resolveRelative(fileData.slug!, file.slug!)} class="internal">
                      {title}
                    </a>
                    <span class="overlap-badge">{overlap} tags</span>
                  </div>
                  <ul class="tags">
                    {tags.slice(0, 3).map((tag) => (
                      <li>
                        <a
                          class="internal tag-link"
                          href={resolveRelative(fileData.slug!, `tags/${tag}` as FullSlug)}
                        >
                          {tag}
                        </a>
                      </li>
                    ))}
                  </ul>
                </div>
              </li>
            )
          })}
        </ul>
      </div>
    )
  }

  RelatedNotes.css = style + `
    .related-notes {
      margin-top: 2rem;
    }

    .related-notes h3 {
      font-family: var(--headerFont);
      font-size: 1rem;
      margin-bottom: 0.75rem;
      color: var(--dark);
    }

    .related-ul {
      list-style: none;
      padding: 0;
      margin: 0;
    }

    .related-li {
      margin-bottom: 0.75rem;
      padding: 0.5rem;
      border-radius: 4px;
      background: var(--highlight);
    }

    .related-li .section {
      display: flex;
      flex-direction: column;
      gap: 0.25rem;
    }

    .related-li .desc {
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .related-li a.internal {
      color: var(--secondary);
      text-decoration: none;
      font-weight: 500;
    }

    .related-li a.internal:hover {
      text-decoration: underline;
    }

    .overlap-badge {
      font-size: 0.7rem;
      background: var(--secondary);
      color: var(--light);
      padding: 0.1rem 0.4rem;
      border-radius: 3px;
    }

    .related-li .tags {
      list-style: none;
      padding: 0;
      margin: 0;
      display: flex;
      flex-wrap: wrap;
      gap: 0.3rem;
    }

    .related-li .tags li {
      font-size: 0.75rem;
    }

    .related-li .tag-link {
      color: var(--darkgray);
      text-decoration: none;
    }

    .related-li .tag-link:hover {
      color: var(--secondary);
    }
  `

  return RelatedNotes
}) satisfies QuartzComponentConstructor
