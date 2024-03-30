# Classificeren-van-Organisaties
de automatische classificatie van organisaties Gezondheid, Sport en Onderwijs
Organisatie Classificatie Script

Dit Python-script biedt een efficiënte oplossing voor het automatisch classificeren van organisaties op basis van hun naam. Door vooraf gedefinieerde trefwoordregels toe te passen, kan het script de industrie identificeren waartoe elke organisatie behoort, wat essentieel is voor databeheer en gerichte marketingstrategieën. Dit document begeleidt je door de installatie, configuratie en het gebruik van dit script.

## Installatie

Voordat je begint, zorg ervoor dat je de volgende vereisten hebt geïnstalleerd op je systeem:

    Python 3.6 of hoger
    pandas library
    openpyxl library (voor het lezen/schrijven van Excel-bestanden)

Je kunt pandas en openpyxl installeren via pip met de volgende commando's:

    bash

    pip install pandas
    pip install openpyxl

## Configuratie

Trefwoord Regels Definiëren: Voordat je het script uitvoert, moet je de trefwoord_regels variabele in het script configureren. Dit is een woordenboek waarin elke sleutel een industrie vertegenwoordigt en elke waarde een lijst van trefwoorden bevat die geassocieerd zijn met die industrie.

Invoerbestand Voorbereiden: Je invoer moet een Excel-bestand zijn dat de namen van organisaties bevat. Zorg ervoor dat de kolom met organisatienamen correct is benoemd zodat het script deze kan herkennen.

## Gebruik

Om het script te gebruiken, volg deze stappen:

Open het script in je favoriete Python-editor of IDE.
    
Pas de invoer_bestand en uitvoer_bestand variabelen aan het begin van het script aan om het pad naar je invoer-Excel-bestand en de gewenste locatie voor het uitvoer-bestand aan te geven.

Voer het script uit. Het script leest je invoerbestand, classificeert elke organisatie op basis van de gedefinieerde trefwoordregels, en slaat het resultaat op in het opgegeven uitvoerbestand.

    
## Voorbeeld

Stel, je hebt een Excel-bestand organisaties.xlsx met een kolom ORG_NAAM die de namen van de organisaties bevat. Na het configureren van de trefwoordregels en het uitvoeren van het script, zal het script een nieuw Excel-bestand geclassificeerde_organisaties.xlsx genereren met een toegevoegde kolom Industrie Classificatie, die de geïdentificeerde industrie voor elke organisatie aangeeft.
Bijdragen

Bijdragen aan dit project zijn welkom! Voel je vrij om fork te maken, aanpassingen te doen, en pull requests te sturen voor eventuele verbeteringen, nieuwe features, of bug fixes.
Licentie

Dit project is gelicenseerd onder de MIT Licentie - zie het LICENSE bestand voor details.
