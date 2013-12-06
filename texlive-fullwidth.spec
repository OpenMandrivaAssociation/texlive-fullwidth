# revision 24684
# category Package
# catalog-ctan /macros/latex/contrib/fullwidth
# catalog-date 2011-11-28 12:38:18 +0100
# catalog-license lppl
# catalog-version 0.1
Name:		texlive-fullwidth
Version:	0.1
Release:	4
Summary:	Adjust margins of text block
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fullwidth
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fullwidth.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fullwidth.doc.tar.xz
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.1-2
+ Revision: 752160
- Rebuild to reduce used resources

* Fri Dec 09 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.1-1
+ Revision: 739618
- texlive-fullwidth
- texlive-fullwidth

