pull:
	@/bin/bash ./scripts/pull.sh

push:
	@/bin/bash ./scripts/push.sh

install-config:
	@/bin/bash ./scripts/install.sh

clean:
	@rm -rf ~/.config/

install-packages:
	@/bin/bash ./scripts/pkgInstall.sh

install: install-packages
	install-config
