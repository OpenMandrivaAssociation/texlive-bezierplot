Name:		texlive-bezierplot
Version:	51398
Release:	2
Summary:	Approximate smooth function graphs with cubic bezier splines for use with TikZ or MetaPost
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/bezierplot
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bezierplot.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/bezierplot.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package consists of a Lua program as well as a (Lua)LaTeX
.sty file. Given a smooth function, bezierplot returns a smooth
bezier path written in TikZ notation (which also matches
MetaPost) that approximates the graph of the function. For
polynomial functions of degree [?] 3 and their inverses the
approximation is exact (up to numeric precision). bezierplot
also finds special points such as extreme points and inflection
points and reduces the number of used points.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/lualatex/bezierplot
%doc %{_texmfdistdir}/doc/lualatex/bezierplot

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
