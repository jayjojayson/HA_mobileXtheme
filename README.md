# 📱 HA_mobileXtheme 📱
This is mobileXtheme for HomeAssistant works with (auto-entities)

Hier möchte ich euch mein mobile Dashboard vorstellen. Das Dashboard basiert auf der auto-entities-card und ermöglicht es ein ausgefülltes Dashboard ohnes weiteres Zutun zu erhalten.
Die Startseite kann nach belieben gestaltet werden. Alle anderen Raum- und Unterseiten werden automatisch mit euren Smarthomegeräten gefüllt. Probiert es aus. 😊


## 📂 Seitenaufbau
Im unteren Menü sind alle Räume aufgeführt. Aktuell sind das Wohzimmer, Küche, Bad, Schlafzimmer, Esszimmer, Flur, Garten und Einstellungen. Es wird also ein 3-Raumwohnung mit Garten dargestellt.
Die Räume können aber auch einfach ediert werden. Wie das geht findet ihr weiter unten in den Erklärungen. Im oberen Menü findet ihr die Unterseiten Verbraucher, Solar, History, Batterie und Luftreiniger.
Auf Startseite habe ich zwei Menüs für den Header hinterlegt. Wählt das gewünschte aus und löscht das andere. Es werden nicht alle Luftreiniger haben, daher ist das zweite Menü an dieser Stelle mit den Einstellungen verknüpft.

## 📖 Features

- #### 📣 Topmenü verstecken über Button (optional)
- #### ⭐ Hauptseiten für alle Räume (Wohzimmer, Küche, Bad, Schlafzimmer, Esszimmer, Flur, Garten und Einstellungen)
- #### ⭐ Unterseiten für Einstellungen, (Verbraucher, Solar, 📈 History, Batterie und Luftreiniger)
- #### ⚡ Seite Einstellungen mit Button um Topheader von HomeAssistant auszublenden
- #### ⚡ Seite Einstellungen mit Verknüpfungen zu euren Geräten, Automatisierungen, Bereichen und Entwickler-Tools
- #### ☀️ Startseite anpassbar (bereits einige Beispiel für Grundaufbau enthalten)
- #### 💻 Raumanpassung einfach möglich (Erklärung dazu, weiter unten)

...coming soon

#### Hauptseiten

#### Unterseiten


## ✔️ Voraussetzungen

Folgende Cards müssen über HACS installiert sein, dass im Anschluss euer kopierter Code funktioniert.
Ich habe bewusst auf wenig zusätzliche Installationen geachtet, es soll ein einfach Einstieg sein.

#### zwingend notwendig
- auto-entities-card
- stack in card
- bubble card

(optional - Topmenu verstecken)
- kiosk mode

#### Sensoren
Es sind keine Sensoren aktuell notwendig.

## 📥 Installation
1. Wähle den YAML-Code aus einer Vorlage und kopiere den Code.
2. Gehe zu deinem Dashboard und füge den kopierten Code direkt in eine neue Seite ein.
4. Schaue das Ergebnis an.

5. Gestaltete Startseite nach deinen Wünschen.

## 💬 Topmenü Hack

Um das Topmenü auf Tablet und Handy auszublenden nutze ich den Kiosk Mode von HACS.
Einfach über HACS installieren und im Anschluss folgenden Code im Raw-Konfigurationseditor an erster Stelle einfügen.
Erreichbar ist der Editor über die drei Punkte oben rechts, wenn man im Bearbeitungsmodus für das Dashboard ist.

Zusätzlich müsst ihr unter Geräte & Dienste einen Helfer mit dem Typ Schalter und Namen kioskmode angelegen. Somit könnt ihr bequem per Schalter das Topmenü ein- oder ausblenden. Ich habe den Schalter in der Unterseite Einstellungen hinterlegt.

```bash
kiosk_mode:
  non_admin_settings:
    hide_header: true
    hide_menubutton: true
    ignore_entity_settings: true
  entity_settings:
    - entity:
        input_boolean.kioskmode: 'on'
      hide_header: true
    - entity:
        input_boolean.kioskmode: 'off'
      hide_header: false
```

## 👩‍💻 Sourcecode Yaml

#### ` Note: Danke an die Entwickler der Cards aus meinen Voraussetzungen. Dadurch wird das Dahsboard zu dem, was es ist. 🤗` 
