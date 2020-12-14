pull:
	@/bin/bash ./scripts/pull.sh

push:
	@/bin/bash ./scripts/push.sh

install:
	echo "Installing config files"
	@/bin/bash ./scripts/install.sh

clean:
	echo "Removing .config file from home folder"
	@rm -rf ~/.config/

packages:
	echo "Installing all packages"
	@/bin/bash ./scripts/pkgInstall.sh

