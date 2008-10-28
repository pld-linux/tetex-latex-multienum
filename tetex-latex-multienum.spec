
%define short_name multienum
%define	texhash	[ ! -x %{_bindir}/texhash ] || %{_bindir}/texhash 1>&2 ;

Summary:	Multi-column enumerated lists
Summary(hu.UTF-8):	Több oszlopos számozott lista.
Name:		tetex-latex-%{short_name}
Version:	1.0
Release:	1
License:	LaTeX Project Public License
Group:		Applications/Publishing/TeX
Source0:	http://tug.ctan.org/get/macros/latex/contrib/multenum.zip
# Source0-md5:	9d825be0ee818aa5ff76dc9f7f42317c
Requires(post,postun):	/usr/bin/texhash
Requires:	tetex-latex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Defines an environment multienumerate, that produces an enumerated
array in which columns are vertically aligned on the counter. The
motivation was lists of answers for a text book, where there are many
rather small items; the multienumerate environment goes some way to
making such lists look neater.

%description -l hu.UTF-8
A 'multienumerate' környezet definíciója, amely egy számozott listát
készít, amelyben az oszlopok a számozáshoz igazodnak. A motivációja az
volt, hogy vannak válaszok rövid listái, amelyet valahogy el kell
helyezni; a 'multienumerate' környezet épp ezt oldja meg.

%prep
%setup -q -n multenum

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

install %{short_name}.sty $RPM_BUILD_ROOT%{_datadir}/texmf/tex/latex/%{short_name}

install -d $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/%{short_name}
install %{short_name}.{article,pdf,sample} $RPM_BUILD_ROOT%{_datadir}/texmf/doc/latex/%{short_name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%texhash

%postun
%texhash

%files
%defattr(644,root,root,755)
%{_datadir}/texmf/tex/latex/%{short_name}
%{_datadir}/texmf/doc/latex/%{short_name}
