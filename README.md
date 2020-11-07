# ytuploaderbyESP


Problem jest jeden którego nie da sie przeskoczyć (przynajmniej ja nie wiem jak)

OPIS PROBLEMU:
///////////////////////////////////////////////////////////
"errors": [
   {
    "domain": "youtube.quota",
    "reason": "quotaExceeded",
    "message": "The request cannot be completed because you have exceeded your \u003ca href=\"/youtube/v3/getting-started#quota\"\u003equota\u003c/a\u003e."
   }
  ],
  "code": 403,
  "message": "The request cannot be completed because you have exceeded your \u003ca href=\"/youtube/v3/getting-started#quota\"\u003equota\u003c/a\u003e." analytics cookies to understand how
  /////////////////////////////////////////////////////////////////
  
Youtube nie daje ci 10000 zapytań dziennie, dają ci 10000 jednostek dziennie; zapytanie może składać się z wielu jednostek, w zależności od tego, co robisz:

Prosta operacja odczytu, która pobiera tylko identyfikator każdego zwróconego zasobu, ma koszt około 1 jednostki.

Operacja zapisu kosztuje około 50 jednostek.

Przesyłanie wideo kosztuje około 1600 jednostek.

Co wystarcza na przesłanie OK 5 filmów na raz :(.

