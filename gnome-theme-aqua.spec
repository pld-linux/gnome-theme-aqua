Summary:	Aqua theme from MacOS X
Summary(pl):	Temat aqua z MacOS X
Name:		gnome-theme-aqua
Version:	1.0
Release:	1
License:	Free
Group:		X11/Amusements
Source0:	http://www.lucidus.uklinux.net/metathemes/metatheme-aqua-%{version}.tar.gz
URL:		http://sunshineinabag.co.uk/
BuildRequires:	bzip2
BuildRequires:	tar
BuildRequires:	xmms-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	gtk-theme-aqua
Requires:	nautilus-theme-aqua
Requires:	sawfish-theme-aqua
Requires:	xmms-skin-aqua
BuildArch:	noarch

%define		_prefix		/usr/X11R6
%define		_xmmsskinsdir	%(xmms-config --data-dir)/Skins

%description
Aqua theme from MacOS X for GTK, Nautilus, Sawfish and XMMS.

%description -l pl
Temat aqua z MacOS X dla GTK, Nautilusa, Sawfisza i XMMS-a.

%package -n xmms-skin-aqua
Summary:	Aqua skin
Summary(pl):	Skórka aqua
Group:		X11/Amusements
Requires:	tar
Requires:	bzip2
Requires:	xmms

%description -n xmms-skin-aqua
Aqua skin. You may be interested in gnome-theme-aqua package.

%description -n xmms-skin-aqua -l pl
Skórka aqua. Mo¿na te¿ spróbowaæ pakietu gnome-theme-aqua.

%package -n gtk-theme-aqua
Summary:	Aqua theme
Summary(pl):	Temat aqua
Group:		Themes/Gtk
Requires:	gtk-engines

%description -n gtk-theme-aqua
An aqua-like theme. You may be interested in gnome-theme-aqua package.

%description -n gtk-theme-aqua -l pl
Temat bazuj±cy na aqua. Mo¿na te¿ spróbowaæ pakietu gnome-theme-aqua.

%package -n nautilus-theme-aqua
Summary:	Aqua theme
Summary(pl):	Temat aqua
Group:		X11/Amusements
Requires:	nautilus

%description -n nautilus-theme-aqua
An aqua-like theme. You may be interested in gnome-theme-aqua package.

%description -n nautilus-theme-aqua -l pl
Temat bazuj±cy na aqua. Mo¿na te¿ spróbowaæ pakietu gnome-theme-aqua.

%package -n sawfish-theme-aqua
Summary:	Aqua theme
Summary(pl):	Temat aqua
Group:		X11/Amusements
Requires:	sawfish

%description -n sawfish-theme-aqua
An aqua-like theme. You may be interested in gnome-theme-aqua package.

%description -n sawfish-theme-aqua -l pl
Temat bazuj±cy na aqua. Mo¿na te¿ spróbowaæ pakietu gnome-theme-aqua.

%prep
%setup -q -n metatheme-aqua-1.0

%build
# xmms section
cd xmms/Winamp_X_XMMS_1.01
tar cf - * | bzip2 -c > ../../Aqua.tar.bz2
cd -

# gtk section
cd gtk/Aqua/gtk
rm -rf ../ICON.png .xvpics
mv gtkrc dupa
echo "pixmap_path \"%{_datadir}/themes/Aqua/gtk\"" > gtkrc
cat dupa >> gtkrc
rm dupa
cd -

# nautilus section
cd nautilus/aqua
find . -type d -name .xvpics -exec rm -rf \{\} \; || /bin/true
rm -rf .thumbnails
cd -

# sawfish section
cd sawfish/AquaX
rm .theme.jl.swp COPYING
rm -rf patches
cd -

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_xmmsskinsdir},%{_datadir}/themes,%{_pixmapsdir}/nautilus,%{_datadir}/sawfish/themes}

install Aqua.tar.bz2 $RPM_BUILD_ROOT%{_xmmsskinsdir}
mv gtk/Aqua $RPM_BUILD_ROOT%{_datadir}/themes
mv nautilus/aqua $RPM_BUILD_ROOT%{_pixmapsdir}/nautilus
mv sawfish/AquaX $RPM_BUILD_ROOT%{_datadir}/sawfish/themes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
# there is some tool for multi theme applying, but it requres gnome2, so
# this package is just to install all below packages

%files -n xmms-skin-aqua
%defattr(644,root,root,755)
%{_xmmsskinsdir}/Aqua.tar.bz2

%files -n gtk-theme-aqua
%defattr(644,root,root,755)
%{_datadir}/themes/Aqua

%files -n nautilus-theme-aqua
%defattr(644,root,root,755)
%{_pixmapsdir}/nautilus/aqua

%files -n sawfish-theme-aqua
%defattr(644,root,root,755)
%{_datadir}/sawfish/themes/AquaX
