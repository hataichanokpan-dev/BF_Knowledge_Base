import { QuartzComponent, QuartzComponentConstructor, QuartzComponentProps } from "./types"
import { classNames } from "../util/lang"

interface Options {
  wordsPerMinute: number
  showLabel: boolean
}

const defaultOptions: Options = {
  wordsPerMinute: 200, // Thai reading speed
  showLabel: true,
}

export default ((userOpts?: Partial<Options>) => {
  const opts = { ...defaultOptions, ...userOpts }

  const ReadingTime: QuartzComponent = ({
    fileData,
    displayClass,
    cfg,
  }: QuartzComponentProps) => {
    const text = fileData.text
    if (!text) return null

    // Count words (Thai and English)
    const wordCount = text.trim().split(/\s+/).length

    // Calculate reading time
    const minutes = Math.ceil(wordCount / opts.wordsPerMinute)

    // Format display
    const displayText = minutes < 1 ? "1 นาที" : `${minutes} นาที`

    return (
      <div class={classNames(displayClass, "reading-time")}>
        <span class="reading-time-icon">📖</span>
        <span class="reading-time-text">{displayText}</span>
      </div>
    )
  }

  ReadingTime.css = `
    .reading-time {
      display: inline-flex;
      align-items: center;
      gap: 0.3rem;
      font-size: 0.85rem;
      color: var(--gray);
      margin-bottom: 0.5rem;
    }

    .reading-time-icon {
      font-size: 0.9rem;
    }

    .reading-time-text {
      font-family: var(--bodyFont);
    }
  `

  return ReadingTime
}) satisfies QuartzComponentConstructor
