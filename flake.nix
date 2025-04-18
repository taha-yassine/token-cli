{
  description = "Python devshell";

  inputs = {
    nixpkgs.url = "nixpkgs/nixos-unstable";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, flake-utils }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = nixpkgs.legacyPackages.${system};

        package = pkgs.python3.pkgs.buildPythonApplication rec {
          pname = "token-cli";
          version = "0.1.0";
          src = self;

          pyproject = true;

          build-system = with pkgs.python3.pkgs; [
            setuptools
            wheel
          ];

          dependencies = with pkgs.python3.pkgs; [
            rich
            tiktoken
          ];
        };

        libs = [
          pkgs.stdenv.cc.cc.lib
          pkgs.zlib
        ];

        shell = pkgs.mkShell {
          packages = with pkgs; [
            python312
            uv
            vhs
          ];
          env = {
            CC = "${pkgs.gcc}/bin/gcc";
            LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath libs;
          };
        };
      in {
        packages.token-cli = package;
        packages.default = self.packages.${system}.token-cli;

        devShells.default = shell;
      }
    );
}
