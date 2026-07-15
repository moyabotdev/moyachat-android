# MoyaChat für Android

Sichere, private Chat-App für den Snikket/XMPP-Server **chat.moyarossiya.com**.

Basiert auf [Snikket Android](https://github.com/snikket-im/snikket-android)
(seinerseits ein Fork von [Conversations](https://conversations.im/) von Daniel Gultsch),
umgebrandet auf **MoyaChat** (App-ID `com.moyarossiya.chat`).

## Installieren / Testen

Neuester Test-Build (Sideload-APK):
**https://github.com/moyabotdev/moyachat-android/releases/download/latest/MoyaChat.apk**

Auf dem Gerät "Unbekannte Quellen zulassen", APK öffnen, installieren. Anmeldung
über Einladungslink oder mit bestehendem Konto (`name@chat.moyarossiya.com`).

## Bauen

    export JAVA_HOME=<JDK 21>
    ./gradlew :assembleConversationsFreeDebug

Ausgabe unter `build/outputs/apk/conversationsFree/debug/`. CI baut bei jedem Push auf
`main` automatisch und hängt die universelle APK ans `latest`-Release
(siehe `.github/workflows/build.yml`).

## Lizenz

GPLv3 (siehe [LICENSE](LICENSE)) — als Conversations/Snikket-Derivat.
