#!/usr/bin/env bash
install_extension() {
    /usr/bin/code --install-extension $1
    /usr/bin/code-insiders --install-extension $1
}

# Install VS Code extensions into VS Code in desktop so we can try
install_extension ms-vscode-remote.remote-containers
install_extension yzhang.markdown-all-in-one
install_extension wholroyd.jinja
install_extension VisualStudioExptTeam.vscodeintellicode
install_extension VisualStudioExptTeam.intellicode-api-usage-examples
install_extension ultram4rine.sqltools-clickhouse-driver
install_extension streetsidesoftware.code-spell-checker
install_extension streetsidesoftware.code-spell-checker-russian
install_extension redhat.vscode-yaml
install_extension redhat.vscode-xml
install_extension njpwerner.autodocstring
install_extension mtxr.sqltools
install_extension mtxr.sqltools-driver-pg
install_extension mtxr.sqltools-driver-mysql
install_extension ms-vscode.test-adapter-converter
install_extension ms-vscode.remote-repositories
install_extension ms-vscode.makefile-tools
install_extension ms-vscode.azure-repos
install_extension ms-toolsai.vscode-jupyter-slideshow
install_extension ms-toolsai.vscode-jupyter-cell-tags
install_extension ms-toolsai.jupyter
install_extension ms-toolsai.jupyter-renderers
install_extension ms-toolsai.jupyter-keymap
install_extension ms-python.vscode-pylance
install_extension ms-python.python
install_extension ms-python.pylint
install_extension ms-python.isort
install_extension ms-python.flake8
install_extension ms-azuretools.vscode-docker
install_extension mhutchie.git-graph
install_extension humao.rest-client
install_extension hbenl.vscode-test-explorer
install_extension Gruntfuggly.todo-tree
install_extension github.remotehub
install_extension funkyremi.vscode-google-translate
install_extension formulahendry.code-runner
install_extension esbenp.prettier-vscode
install_extension eamodio.gitlens
install_extension DotJoshJohnson.xml
install_extension donjayamanne.python-environment-manager
install_extension adpyke.vscode-sql-formatter
install_extension aaron-bond.better-comments
install_extension GitHub.remotehub