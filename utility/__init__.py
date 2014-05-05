__all__ = [
		"file",
		"attribute",
		"constraint",
		"control",
		"curve",
		"file",
		"joint",
		"lib",
		"stringLib",
		"transform"
]

from UtilitiesPackage.File import mayaImport, mayaImportAll, package_contents

for module in package_contents("UtilitiesPackage"):
	if module != "__init__":
		exec mayaImport( module )
		exec mayaImportAll( module )

