# backup-trello
Utility to devendor-lock onself from Atlasian

At the time of creation I have a Trello board with 1k+ cards. I'm gradually reducing my dependency on Trello, however frequent backups are the sweet spot for ensuring that my data won't be held hostage or disappear all of a sudden.

## Usage
For now go for [dev](#dev)

## Dev

### Prerequisites
- [nix](https://nixos.org/download.html)
- `direnv` (`nix-env -iA nixpkgs.direnv`)
- [configured direnv shell hook ](https://direnv.net/docs/hook.html)
- some form of `make` (`nix-env -iA nixpkgs.gnumake`)

Hint: if something doesn't work because of missing package please add the package to `default.nix` instead of installing it on your computer. Why solve the problem for one if you can solve the problem for all? ;)

### One-time setup
```
make init
```

### Everything
```
make help
```
