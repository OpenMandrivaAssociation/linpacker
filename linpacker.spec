%define name linpacker
%define version 0.7.1
%define release %mkrel 1

Summary:        Tool for 2D bin packing
Name:           %{name}
Version:        %{version}
Release:        %{release}
License:        GPL
Group:          Sciences/Mathematics
URL:            http://freehackers.org/~tnagy/linpacker/
Source0:        http://freehackers.org/~tnagy/linpacker/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-buildroot
BuildRequires:	qt4-devel 
BuildRequires:	kdelibs-devel
BuildRequires:	python
BuildRequires:	desktop-file-utils
Provides:	LinPacker = %version-%release
Obsoletes:	LinPacker < 0.5.9-3
Requires(post):	desktop-file-utils
Requires(postun):	desktop-file-utils
%description
Tool for 2D Bin Packing

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q 

%build

./waf configure --prefix=%_prefix/ --qtdir=/usr/lib/qt4/ --want-rpath=0
./waf %_smp_mflags

%install
./waf install --destdir=%buildroot

# icon
install -D -m 644 $RPM_BUILD_ROOT%_iconsdir/hicolor/16x16/apps/%{name}.png $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png
install -D -m 644 $RPM_BUILD_ROOT%_iconsdir/hicolor/32x32/apps/%{name}.png $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
install -D -m 644 $RPM_BUILD_ROOT%_iconsdir/hicolor/48x48/apps/%{name}.png $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat >$RPM_BUILD_ROOT%{_menudir}/%{name} <<EOF
?package(%{name}):\
command="%{_bindir}/%{name}"\
title="LinPacker"\
longtitle="Places rectangular shapes."\
needs="KDE"\
section="Applications/Sciences/Mathematics"\
icon="%{name}.png"\
xdg="true"
EOF

desktop-file-install --vendor="" \
  --delete-original \
  --add-category "X-MandrivaLinux-MoreApplications-Sciences-Mathematics" \
  --add-mime-type "application/x-linpacker" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applnk/*/*

chmod 644 README 
rm -f $RPM_BUILD_ROOT%_prefix/doc/packages/linpacker/test.lnpk

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT 

%post
%{update_menus}
%update_icon_cache hicolor
%{update_desktop_database}

%postun
%{clean_menus}
%clean_icon_cache hicolor
%{clean_desktop_database}

%files -f %name.lang
%defattr(-,root,root,0755)
%doc README test.lnpk
%{_bindir}/*
%_datadir/applications/linpacker.desktop
%_datadir/mimelnk/application/x-linpacker.desktop
%_iconsdir/hicolor/16x16/apps/linpacker.png
%_iconsdir/hicolor/32x32/apps/linpacker.png
%_iconsdir/hicolor/48x48/apps/linpacker.png
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%_menudir/%{name}



