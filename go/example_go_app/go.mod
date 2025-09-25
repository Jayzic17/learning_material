// All files and folders must belong to a Go application (Module)
// The 'module' command tells Go which Go application all the files and folders under this directory belongs to
module example_go_app

// Anything specified in the 'require' command is also itself a Go application (Module)
require github.com/pkg/errors v0.9.1

go 1.25.1
