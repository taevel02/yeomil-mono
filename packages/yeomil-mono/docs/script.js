document.addEventListener("DOMContentLoaded", () => {
  // DOM Elements
  const playground = document.getElementById("font-playground");
  const sizeInput = document.getElementById("font-size");
  const sizeVal = document.getElementById("size-val");
  const lhInput = document.getElementById("line-height");
  const lhVal = document.getElementById("lh-val");
  const toggleGrid = document.getElementById("toggle-grid");
  const gridOverlay = document.getElementById("grid-overlay");
  const copyButtons = document.querySelectorAll(".copy-btn");

  // Size adjustment control
  sizeInput.addEventListener("input", (e) => {
    const size = e.target.value;
    sizeVal.textContent = `${size}px`;
    playground.style.fontSize = `${size}px`;
    updateGridSize();
  });

  // Line height adjustment control
  lhInput.addEventListener("input", (e) => {
    const lh = e.target.value;
    lhVal.textContent = lh;
    playground.style.lineHeight = lh;
  });

  // Update background-size of grid overlay dynamically based on character width
  function updateGridSize() {
    // 1ch in monospace is exactly the width of the '0' glyph (latin width = 600 units)
    // 2ch represents 1200 units, which is exactly 1 CJK character width.
    // We set background-size to 2ch so every vertical grid line represents 1 CJK or 2 Latin characters.
    gridOverlay.style.backgroundSize = `calc(2ch) 100%`;
  }

  // Toggle grid guidelines
  toggleGrid.addEventListener("change", (e) => {
    if (e.target.checked) {
      gridOverlay.style.opacity = "1";
    } else {
      gridOverlay.style.opacity = "0";
    }
  });

  // Copy buttons interaction
  copyButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      const textToCopy = btn.getAttribute("data-copy");
      navigator.clipboard.writeText(textToCopy).then(() => {
        const originalText = btn.textContent;
        btn.textContent = "Copied!";
        btn.classList.add("copied");
        
        setTimeout(() => {
          btn.textContent = originalText;
          btn.classList.remove("copied");
        }, 2000);
      }).catch((err) => {
        console.error("Copy failed.", err);
      });
    });
  });

  // Initial Runs
  updateGridSize();
});
