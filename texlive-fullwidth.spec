Name:		texlive-fullwidth
Version:	24684
Release:	1
Summary:	Adjust margins of text block
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fullwidth
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fullwidth.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fullwidth.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides the environment fullwidth, which sets the
left and right margins in a simple way. There is no constraint
about page breaks; if you are using the twoside mode, you can
set the inner and outer margins to avoid the effects of the
different margins.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/fullwidth/fullwidth.sty
%doc %{_texmfdistdir}/doc/latex/fullwidth/README
%doc %{_texmfdistdir}/doc/latex/fullwidth/fullwidth-test.pdf
%doc %{_texmfdistdir}/doc/latex/fullwidth/fullwidth-test.tex
%doc %{_texmfdistdir}/doc/latex/fullwidth/fullwidth.pdf
%doc %{_texmfdistdir}/doc/latex/fullwidth/fullwidth.tex

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
