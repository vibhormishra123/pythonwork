$breakpoints: (
  mobile: 375px,
  tablet: 768px,
  // etc.
);

// Sass variables for writing out media queries
$media: (
  mobile: '(max-width: #{map-get($breakpoints, mobile)})',
  tablet: '(max-width: #{map-get($breakpoints, tablet)})',
  // etc.
);

// The export module that makes Sass variables accessible in JavaScript
:export {
  breakpointMobile: unquote(map-get($media, mobile));
  breakpointTablet: unquote(map-get($media, tablet));
  // etc.
}