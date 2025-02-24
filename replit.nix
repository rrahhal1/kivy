
{pkgs}: {
  deps = [
    pkgs.nano
    pkgs.autoconf271
    pkgs.unzipNLS
    pkgs.wget
    pkgs.splat
    pkgs.pkg-config
    pkgs.zlib
    pkgs.zlib.dev
    pkgs.mtdev
    pkgs.libcxx
    pkgs.SDL2_ttf
    pkgs.SDL2_mixer
    pkgs.SDL2_image
    pkgs.SDL2
    pkgs.xcbuild
    pkgs.swig
    pkgs.openjpeg
    pkgs.mupdf
    pkgs.libjpeg_turbo
    pkgs.jbig2dec
    pkgs.harfbuzz
    pkgs.gumbo
    pkgs.freetype
    pkgs.xsel
    pkgs.buildPackages.gcc
    pkgs.python311
    pkgs.android-tools
    pkgs.jdk17
  ];
}
