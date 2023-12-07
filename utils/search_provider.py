from rdflib import Graph

def seach_by_provider(provider):
    g = Graph()
    g.parse('coursera_csv (1).ttl', format='turtle')

    # Query for retrieving course by provider
    query = f"""
    prefix : <https://www.coursera.org/>
    prefix owl: <http://www.w3.org/2002/07/owl#>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix xml: <http://www.w3.org/XML/1998/namespace>
    prefix xsd: <http://www.w3.org/2001/XMLSchema#>
    prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    prefix vcard: <http://www.w3.org/2006/vcard/ns#>

    select distinct ?course ?price ?title ?skills ?ratings ?reviews ?level ?type ?duration
    where {{
        ?course :price ?price ;
                :course_by :{provider} ;
                :title ?title;
                :skills ?skills ;
                :ratings ?ratings ;
                :level ?level ;
                :type ?type ;
                :duration ?duration .
    }}
    """
    results = g.query(query)

    return results