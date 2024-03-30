import pandas as pd

def classificeer_organisatie(naam, trefwoord_regels):
    """
    Classificeer de organisatie op basis van de naam met vooraf gedefinieerde trefwoordregels.

    :param naam: De naam van de organisatie.
    :param trefwoord_regels: Een woordenboek waarbij de sleutels de industrie classificaties zijn en
                             de waarden lijsten met trefwoorden geassocieerd met die industrie.
    :return: De voorspelde industrie classificatie.
    """
    for industrie, trefwoorden in trefwoord_regels.items():
        if any(trefwoord.lower() in naam.lower() for trefwoord in trefwoorden):
            return industrie
    return "Onbekende Industrie"

# Trefwoordregels gebaseerd op handmatige identificatie
trefwoord_regels = {
    'Ziekenhuizen en geestelijke gezondheids- en verslavingszorg met overnachting': ['Reinier de Graaf Groep','Woonzorggroep','ziekenhuisgroep','Gezinshuis', 'Woonzorg','Palliatieve','Hospice','Academisch Ziekenhuis','Medische Centrum','Medisch Centrum','Medische Centra','Radboudumc','Erasmus MC','Radboudumc','Amsterdam UMC', 'Leids Universitair Medisch Centrum','Universitair Medisch Centrum Groningen','UMC Utrecht','Universitair Medisch Centrum Utrecht', 'LUMC', 'UMC', 'AMC', 'VuMC', 'UMCG','Ziekenhuis','ziekenhuizen','hospital','Geestelijke gezondheidszorg','ggz', 'GGZ','Zorgthuis', 'Zorgvilla\'s', 'Zorghuys'],
    'Woningbouwverenigingen en -stichtingen': ['Woningbouwvereniging','woningstichting','wonen'],
    'Medische en tandheelkundige praktijken': ['Huisartsencentrum','Orthopedagogische Praktijk','Tandarstpraktijk','Tandartenpraktijk','Mondzorgpraktijk','Tandartpraktijk','Orthodontistenpraktijk','Mondcare','Mondcentrum','Tandhaven','Ortho', 'Mondzorg','Tanzorg','Tandartspraktijk', 'Tandartsenpraktijk', 'Tandarts','Dental', 'Tandheelkundig', 'Tandheelkunde','Medisch Kwartier','huisartenpraktijk','Husiartspraktijk','Huisartsenpraktijk', 'Huisartspraktijk', 'Huisartsen', 'huisartsenpraktijk', 'Huisarts', 'huisarts', 'Huisartsenmaatschap', 'huisartspraktijk','klinieken','clinics'],
    'Apotheek': ['Apotheek', 'apotheek', 'Apotheekhoudende', 'Apotheken'],
    'Maatschappelijke dienstverlening zonder overnachting gericht op ouderen en  gehandicapten': ['Stichting Zorgbureau','Stichting Ouderenzorg','Welzijn','care','zorg','Thuiszorg', 'Thuis'],
    'Paramedische praktijken en overige gezondheidszorg zonder overnachting': ['Instituut','Gezondheidscentrum','Zorgcentra', 'Zorgcentrum', 'Zorggroep','Zorgboerderij','Dagbesteding','Begeleiding','Revalidatie', 'Fysiotherapie', 'Fysio', 'kraamzorg'],
    'Sport': ['Golfclub', 'hockeyclub','tennisclub','golfclub','Zwembaden','Optisport','Hockey', 'Tennis','Golf','Zwemvereniging','Voetbalvereniging', 'Sportvereniging','Tennisvereniging','Sportfondsen','Health', 'Sporthal', 'Sportpark', 'Sport'],
    'Tertiair onderwijs': ['Rijksuniversiteit Groningen','university','Rijksuniversiteit','TU','UT','RUG','universiteit', 'Hogeschool','hogescholen', 'Hogere onderwijs', 'Hogere beroepsonderwijs'], 
    'Primair en speciaal onderwijs':['primair','Prim. Onderwijs','Primair Onderwijs','Speciaal onderwijs', 'Basisonderwijs'],
    'Voortgezet onderwijs':['Havo', 'vwo', 'college', 'Voorbereidend', 'Praktijkonderwijs', 'beroepsonderwijs'],
    'Middelbaar beroepsonderwijs en educatie':['ROC','MBO', 'Middelbaar beroepsonderwijs','Volwassenen onderwijs'],
    'Overige dienstverlenging(voornamelijk zorg aanbieders)': ['Coöperatie','vof', 'V.O.F.', 'V,O,F,'],
    'Jeugdzorg en maatschappelijke opvang met overnachting': ['Jeugd','Jeugdzorg'],
    # Voeg hier uw industrieën en hun geassocieerde trefwoorden toe
}

def verwerk_excel_bestand(invoer_bestand, uitvoer_bestand, trefwoord_regels):
    # Lees het Excel-bestand
    df = pd.read_excel(invoer_bestand)
    
    # Classificeer elke organisatie
    df['Industrie Classificatie'] = df['ORG_NAAM'].apply(lambda x: classificeer_organisatie(x, trefwoord_regels))
    
    # Sla het resultaat op in een nieuw Excel-bestand
    df.to_excel(uitvoer_bestand, index=False)

# Voorbeeld van hoe de functie te gebruiken
invoer_bestand = 'pad_naar_uw_excel_bestand.xlsx'  # Vervang dit door het pad naar uw Excel-bestand
uitvoer_bestand = 'geclassificeerde_organisaties.xlsx'

verwerk_excel_bestand(invoer_bestand, uitvoer_bestand, trefwoord_regels)
