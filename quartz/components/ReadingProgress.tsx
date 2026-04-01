import { QuartzComponentConstructor, QuartzComponentProps } from "./types"

export default (() => {
  function ReadingProgress({ displayClass }: QuartzComponentProps) {
    return (
      <div class={`reading-progress-container ${displayClass ?? ""}`}>
        <div class="reading-progress-bar" id="reading-progress"></div>
      </div>
    )
  }

  ReadingProgress.css = `
    .reading-progress-container {
      position: fixed;
      top: 0;
      left: 0;
      width: 100%;
      height: 3px;
      background: transparent;
      z-index: 1000;
    }

    .reading-progress-bar {
      height: 100%;
      background: var(--secondary);
      width: 0%;
      transition: width 0.05s linear;
    }
  `

  ReadingProgress.afterDOMLoaded = `
    function updateReadingProgress() {
      const progressBar = document.getElementById('reading-progress');
      if (!progressBar) return;

      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const progress = (scrollTop / docHeight) * 100;

      progressBar.style.width = progress + '%';
    }

    window.addEventListener('scroll', updateReadingProgress);
    document.addEventListener('DOMContentLoaded', updateReadingProgress);
    window.addEventListener('resize', updateReadingProgress);
  `

  return ReadingProgress
}) satisfies QuartzComponentConstructor
