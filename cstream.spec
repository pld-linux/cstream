Summary:	A general-purpose streaming tool
Summary(pl.UTF-8):	Narzędzie do strumieni ogólnego przeznaczenia
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

%description -l pl.UTF-8
cstream to ogólnego przeznaczenia narzędzie do obsługi strumieni
podobne do uniksowego dd, zwykle używane w potokach tworzonych z linii
poleceń.

Cechy:
- rozsądna składnia opcji linii poleceń
- ścisłe ograniczanie przepustowości po stronie przychodzącej;
  odchylenie czasu w poprzednich odczytach jest równoważone w
  następnych
- precyzyjne zgłaszanie przepustowości - na końcu transmisji lub po
  każdym otrzymaniu SIGUSR1, co jest dość przydatne podczas długich
  operacji, aby sprawdzić ile już przesłano; raporty są wypisywane w
  bajtach/sekundę oraz ew. w KB/s lub MB/s (1K=1024)
- SIGHUP powoduje czyste zakończenie programu przed otrzymaniem EOF z
  wejścia; wyświetlane są przy tym informacje o czasie
- wbudowana obsługa zapisu PID-u do pliku w celu bezbolesnego
  wysyłania ww. sygnałów
- wbudowana obsługa potoków nazwanych (fifo); przykładowe zastosowanie
  to "pseudo-urządzenie" pochłaniające lub dostarczające dane z
  odpowiednią częstotliwością, ale wyglądające jak plik - np. do
  testowania oprogramowania do obsługi kart dźwiękowych; szczegóły na
  stronie manuala
- wbudowane tworzenie i pochłanianie danych - nie trzeba
  przekierowywać /dev/null czy /dev/zero; szybkość tych urządzeń
  specjalnych różni się znacząco między systemami operacyjnymi, więc
  przekierowywanie ich nie jest odpowiednie przy testach szybkości, a
  jest marnowaniem zasobów
- przyjmuje znaki 'k', 'm' i 'g' (oznaczające kilo, mega i giga) po
  liczbie ograniczenia rozmiaru danych
- kod czysty pod kątem "gcc -Wall", szczególny nacisk został położony
  na unikanie zachowań nieokreślonych przez ANSI C czy POSIX, z
  wyjątkiem wymagania long long; ograniczanie i raportowanie działa na
  ilościach danych powyżej 4 GB.

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
