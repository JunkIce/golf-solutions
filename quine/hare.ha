// Bytes
use fmt;
const src: str = "use fmt;
const src: str = {0}{1}{0};
export fn main() void = {{fmt::printfln(src, '{0}', src)!;}};";
export fn main() void = {fmt::printfln(src, '"', src)!;};

// --
// Chars
// (same as bytes)
