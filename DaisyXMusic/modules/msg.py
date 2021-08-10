# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import os
from DaisyXMusic.config import SOURCE_CODE
from DaisyXMusic.config import ASSISTANT_NAME
from DaisyXMusic.config import PROJECT_NAME
from DaisyXMusic.config import SUPPORT_GROUP
from DaisyXMusic.config import UPDATES_CHANNEL
class Messages():
      START_MSG = "**Merhaba 👋 [{}](tg://user?id={})!**\n\n🤖 Ben telegram gruplarına Sesli sohbetlerde Müzik calmak icin yapıldım & Hoşgeldin\n\n✅ Bana  /help yazarak bilgi alabirsin."
      HELP_MSG = [
        ".",
f"""
**Hey ♪ tekrar Hoş Geldiniz {PROJECT_NAME}

⚪️ {PROJECT_NAME} grubunuzun sesli sohbetinde ve kanal sesli sohbetlerinde müzik çalabilir

⚪️ Assistant name >> @{ASSISTANT_NAME}\n\nClick next for instructions**
""",

f"""
**Ayarlama**


1) Beni grubuna al
2)Mesajları görebilmem için yönetici yap  
3)  @{ASSISTANT_NAME}  Grubuna al ve sesli sohbeti aç sonra istediğin şarkıyı dileyebilirsin🥳🥳
** Kanal Müzik Çalma İçin**
1) beni kanalınızın yöneticisi yapın 
2) bağlantılı grupta / userbotjoinchannel Gönder
3) Şimdi bağlantılı grupta komutlar gönderin
""",
f"""
**Komutlar**

**=>> Song Playing 🎧**

- /oynat: Müzüği başlatir
- /oynat: [yt url] : Belirlediginiz Yt url atarsanız calısır
- /oynat: [reply yo audio]: her hangi bi muzigi aratabilirsin

**=>> Playback ⏯**

- /player: Müzük Menüsü Açılır
- /skip: Müzüği atlarsınız
- /pause: Müzik durur
- /resume: Müzik devam eder
- /end: Durur medya lı müzik
- /current: Geçerli çalma parçasını gösterir
- /playlist: Çalma listesini gösterir

*Player cmd ve /play, /current ve /playlist dışındaki diğer tüm cmd'ler yalnızca grubun yöneticileri içindir.
""",
f"""
**=>> Daha fazla araç 🧑🔧**

- /musicplayer [on / off]: müzik çaları Etkinleştir / devre dışı bırak
- /admincache: grubunuzun yönetici bilgilerini günceller. Bot yönetici tarafından tanınmıyorsa deneyin
- /userbotjoin: @{ASSISTANT_NAME} kullanıcısını sohbetinize davet edin
""",
f"""
**=>> Şarkı İndir 🎸**

- /video [şarkı mame]: youtube'dan Video şarkı indir
- /song [şarkı adı]: youtube'dan ses şarkısı indir

"""
      ]
