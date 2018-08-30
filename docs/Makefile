# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SPHINXPROJ    = GirlEffectCoremanagementlayer
SOURCEDIR     = source
BUILDDIR      = build

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	ACCESS_CONTROL_API="foo" USER_DATA_STORE_API="foo" AUTHENTICATION_SERVICE_API="foo" AUTHENTICATION_SERVICE_JWKS="foo" ACCESS_CONTROL_API_KEY="foo" AUTHENTICATION_SERVICE_API_KEY="foo" USER_DATA_STORE_API_KEY="foo" MANAGEMENT_PORTAL_CLIENT_ID="foo" $(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
