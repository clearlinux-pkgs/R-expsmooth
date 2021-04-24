#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-expsmooth
Version  : 2.3
Release  : 22
URL      : https://cran.r-project.org/src/contrib/expsmooth_2.3.tar.gz
Source0  : https://cran.r-project.org/src/contrib/expsmooth_2.3.tar.gz
Summary  : Data Sets from "Forecasting with Exponential Smoothing"
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-forecast
BuildRequires : R-forecast
BuildRequires : buildreq-R

%description
Hyndman, Koehler, Ord and Snyder (Springer, 2008).

%prep
%setup -q -c -n expsmooth
cd %{_builddir}/expsmooth

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589771950

%install
export SOURCE_DATE_EPOCH=1589771950
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library expsmooth
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library expsmooth
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library expsmooth
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc expsmooth || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/expsmooth/DESCRIPTION
/usr/lib64/R/library/expsmooth/INDEX
/usr/lib64/R/library/expsmooth/Meta/Rd.rds
/usr/lib64/R/library/expsmooth/Meta/data.rds
/usr/lib64/R/library/expsmooth/Meta/features.rds
/usr/lib64/R/library/expsmooth/Meta/hsearch.rds
/usr/lib64/R/library/expsmooth/Meta/links.rds
/usr/lib64/R/library/expsmooth/Meta/nsInfo.rds
/usr/lib64/R/library/expsmooth/Meta/package.rds
/usr/lib64/R/library/expsmooth/NAMESPACE
/usr/lib64/R/library/expsmooth/data/Rdata.rdb
/usr/lib64/R/library/expsmooth/data/Rdata.rds
/usr/lib64/R/library/expsmooth/data/Rdata.rdx
/usr/lib64/R/library/expsmooth/help/AnIndex
/usr/lib64/R/library/expsmooth/help/aliases.rds
/usr/lib64/R/library/expsmooth/help/expsmooth.rdb
/usr/lib64/R/library/expsmooth/help/expsmooth.rdx
/usr/lib64/R/library/expsmooth/help/paths.rds
/usr/lib64/R/library/expsmooth/html/00Index.html
/usr/lib64/R/library/expsmooth/html/R.css
