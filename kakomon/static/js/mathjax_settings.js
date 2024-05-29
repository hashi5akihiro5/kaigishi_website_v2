// MathJax設定
window.MathJax = {
    loader: {load: ['[tex]/physics']},
    tex: {
      inlineMath: [['$', '$'], ['\\(', '\\)']],
      displayMath: [['$$', '$$'], ['\\[', '\\]']],
      packages: {'[+]': ['physics']}
    },
    chtml: {
      matchFontHeight: false,
      linebreaks: {
          automatic: true, // CHTML出力に対する自動改行の設定
      }
    },
    svg: {
      linebreaks: {automatic: true} // SVG出力に対する自動改行の設定
    }
  };