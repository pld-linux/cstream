Summary:	A general-purpose streaming tool
Summary(pl):	Narzêdzie do strumieni ogólnego przeznaczenia
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

%description -l pl
cstream to ogólnego przeznaczenia narzêdzie do obs³ugi strumieni
podobne do uniksowego dd, zwykle u¿ywane w potokach tworzonych z linii
poleceñ.

Cechy:
- rozs±dna sk³adnia opcji linii poleceñ
- ¶cis³e ograniczanie przepustowo¶ci po stronie przychodz±cej;
  odchylenie czasu w poprzednich odczytach jest równowa¿one w
  nastêpnych
- precyzyjne zg³aszanie przepustowo¶ci - na koñcu transmisji lub po
  ka¿dym otrzymaniu SIGUSR1, co jest do¶æ przydatne podczas d³ugich
  operacji, aby sprawdziæ ile ju¿ przes³ano; raporty s± wypisywane w
  bajtach/sekundê oraz ew. w KB/s lub MB/s (1K=1024)
- SIGHUP powoduje czyste zakoñczenie programu przed otrzymaniem EOF z
  wej¶cia; wy¶wietlane s± przy tym informacje o czasie
- wbudowana obs³uga zapisu PID-u do pliku w celu bezbolesnego
  wysy³ania ww. sygna³ów
- wbudowana obs³uga potoków nazwanych (fifo); przyk³adowe zastosowanie
  to "pseudo-urz±dzenie" poch³aniaj±ce lub dostarczaj±ce dane z
  odpowiedni± czêstotliwo¶ci±, ale wygl±daj±ce jak plik - np. do
  testowania oprogramowania do obs³ugi kart d¼wiêkowych; szczegó³y na
  stronie manuala
- wbudowane tworzenie i poch³anianie danych - nie trzeba
  przekierowywaæ /dev/null czy /dev/zero; szybko¶æ tych urz±dzeñ
  specjalnych ró¿ni siê znacz±co miêdzy systemami operacyjnymi, wiêc
  przekierowywanie ich nie jest odpowiednie przy testach szybko¶ci, a
  jest marnowaniem zasobów
- przyjmuje znaki 'k', 'm' i 'g' (oznaczaj±ce kilo, mega i giga) po
  liczbie ograniczenia rozmiaru danych
- kod czysty pod k±tem "gcc -Wall", szczególny nacisk zosta³ po³o¿ony
  na unikanie zachowañ nieokre¶lonych przez ANSI C czy POSIX, z
  wyj±tkiem wymagania long long; ograniczanie i raportowanie dzia³a na
  ilo¶ciach danych powy¿ej 4 GB.

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
