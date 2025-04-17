#import "sprache.typ": sprache
// #import "titelseite.typ": titelseite
// #import "inhaltsverzeichnis.typ": toc
#import "ueberschriften.typ": ueberschriften
// #import "abschnitt.typ": abschnitt
// #import "kapitel.typ": kapitel
#import "normaltext.typ": normaltext

#show: sprache
#show: normaltext
#show: ueberschriften

= Vorbereitung

== Die Installation von Python und weiterer Module

In der Regel sollte auf einem Linux-System eine ausreichend aktuelle Python 3-Version installiert sein. Man prüfe:

```shell-unix-generic
nutzer@rechnername:~$ python3 --version
```

== Die Einrichtung des Arbeitsbereichs und einer virtuellen Python-Umgebung

Es wird eine virtuelle Python-Umgebung für das Projekt installiert, damit zusätzliche Python-Module nicht das Gesamtsystem beeinflussen. In VS Code kann eine virtuelle Arbeitsumgebung über die Befehlspallette eingerichtet werden.

- Menü: Anzeigen
- Befehlspallette
- Python: Umgebung erstellen
- Venv

== Die Installation von Briefcase

Man öffne ein neues Terminal. Dort sollte vor den Angaben zu Nutzer, Rechnername und Projektpfad den Ordnernamen der virtuellen Umgebung in runden Klammern stehen.

```bash
(.venv) nutzer@rechnername:~/Projekte/BruchrechenApp$
```

Briefcase wird über das Tool `pip` installiert.

```bash
nutzer@rechnername:~/Projekte/BruchrechenApp$ python3 -m pip install briefcase
```

= Das Projekt für die Bruchrechen-App

== Ein neues Projekt einrichten

```bash
(.venv) $ briefcase new
```

== Die App ausführen

```bash
(.venv) $ cd bruchrechenapp
(.venv) $ briefcase dev
```

= Das Frontend

== Die GUI-Bibliothek Toga

== Die Beispielzeile