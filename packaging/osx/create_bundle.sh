
conda create -p App/CondaTest.app/Contents/Resources \
    testconda lxml  \
    -c stephensmith25 \
    -y

# activate the envi


version_name = '1.0'

conda list -p App/CondaTest.app/Contents/Resources > App/CondaTest.app/Contents/packages.txt
sed -i "1s/.*/\n\nLIST OF PACKAGES:/"  App/CondaTest.app/Contents/packages.txt





