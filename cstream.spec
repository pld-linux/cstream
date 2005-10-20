Summary:	A general-purpose streaming tool
Name:		cstream
Version:	2.6.0
Release:	1
License:	MIT
Group:		Networking/Utilities
Source0:	http://www.cons.org/cracauer/download/%{name}-%{version}.tar.gz
# Source0-md5:	64c3fbc1a2ce0f5a1be812263bb25b42
URL:		http://www.cons.org/cracauer/cstream.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
cstream is a general-purpose stream-handling tool like UNIX dd,
usually used in commandline-constructed pipes.

Features:
- Sane commandline switch syntax.
- Exact throughput limiting, on the incoming side. Timing variance in
  previous reads are counterbalanced in the following reads.
- Precise throughput reporting. Either at the end of the transmission
  or everytime SIGUSR1 is received. Quite useful to ask lengthy
  operations how much data has been transferred yet, i.e. when writing
  tapes. Reports are done in bytes/sec and if appropriate in KB/sec or
  MB/sec, where 1K = 1024.
- SIGHUP causes a clean shutdown before EOF on input, timing
  information is displayed.
- Build-in support to write its PID to a file, for painless sending of
  these signals.
- Build-in support for fifos. Example usage is a 'pseudo-device',
  something that sinks or delivers data at an appropriate rate, but
  looks like a file, i.e. if you test soundcard software. See the
  manpage for examples.
- Built-in data creation and sink, no more redirection of /dev/null
  and /dev/zero. These special devices speed varies greatly among
  operating systems, redirecting from it isn't appropriate benchmarking
  and a waste of resources anyway.
- Accepts 'k', 'm' and 'g' character after number for "kilo, mega,
  giga" bytes for overall data size limit.
- "gcc -Wall" clean source code, serious effort taken to avoid
  undefined behavior in ANSI C or POSIX, except long long is required.
  Limiting and reporting works on data amounts > 4 GB.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man?/*
