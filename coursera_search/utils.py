from rdflib import Graph
from SPARQLWrapper import JSON, SPARQLWrapper
import json

class RDFHandle:
    def __init__(self):
        self.sparql = SPARQLWrapper(
            "http://localhost:9999/blazegraph/namespace/kb/sparql"
        )
        self.sparql.setReturnFormat(JSON)

    def search(self, search_by, query):
        if search_by == 'course':
            return self.search_by_course(query)
        
        elif search_by == 'university':
            return self.search_by_provider(query)
        
        elif search_by == 'price':
            return self.search_by_price(query)
        
        elif search_by == 'skills':
            return self.search_by_skills(query)
        
        elif search_by == 'ratings':
            return self.search_by_ratings(query)
        
        elif search_by == 'level':
            return self.search_by_level(query)
        
        elif search_by == 'type':
            return self.search_by_type(query)
        
        else:
            return self.search_by_provider(query)
    
    def search_by_provider(self, provider):
        # Query for retrieving course by provider
        query = f"""
        prefix : <https://www.coursera.org/>
        prefix owl: <http://www.w3.org/2002/07/owl#>
        prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        prefix xml: <http://www.w3.org/XML/1998/namespace>
        prefix xsd: <http://www.w3.org/2001/XMLSchema#>
        prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix vcard: <http://www.w3.org/2006/vcard/ns#>

        select distinct ?course ?label ?comment ?price ?provider ?title ?skills ?ratings ?reviews ?level ?type ?duration
        where {{
        ?course :price ?price ;
                :course_by ?provider ;
                :title ?title;
                :skills ?skills ;
                :ratings ?ratings ;
                :reviews ?reviews ;
                :level ?level ;
                :type ?type ;
                :duration ?duration .
        
        ?provider :name ?provider_name .

        filter(contains(lcase(?provider_name), lcase("{provider}")))
        SERVICE <https://dbpedia.org/sparql> {{
            OPTIONAl {{
            ?provider rdfs:label ?label ;
                        rdfs:comment ?comment .
            FILTER(LANG(?label) = "en")
            FILTER(LANG(?comment) = "en")
            }}
        }}
        }}
        """
        self.sparql.setQuery(query)
        return self.sparql.queryAndConvert()["results"]["bindings"]
        
    def search_by_course(self, course):
        # Query for retrieving course by provider
        query = f"""
        prefix : <https://www.coursera.org/>
        prefix owl: <http://www.w3.org/2002/07/owl#>
        prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        prefix xml: <http://www.w3.org/XML/1998/namespace>
        prefix xsd: <http://www.w3.org/2001/XMLSchema#>
        prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix vcard: <http://www.w3.org/2006/vcard/ns#>

        select distinct ?course ?label ?comment ?price ?provider ?title ?skills ?ratings ?reviews ?level ?type ?duration
        where {{
        ?course :price ?price ;
                :course_by ?provider ;
                :title ?title;
                :skills ?skills ;
                :ratings ?ratings ;
                :level ?level ;
                :type ?type ;
                :duration ?duration .

        ?provider :name ?provider_name .

        filter(contains(lcase(?title), lcase("{course}")))
        SERVICE <https://dbpedia.org/sparql> {{
            OPTIONAl {{
            ?provider rdfs:label ?label ;
                        rdfs:comment ?comment .
            FILTER(LANG(?label) = "en")
            FILTER(LANG(?comment) = "en")
            }}
        }}
        }}
        """
        self.sparql.setQuery(query)
        return self.sparql.queryAndConvert()["results"]["bindings"]
        
    def search_by_price(self, price):
        # Query for retrieving course by provider
        query = f"""
        prefix : <https://www.coursera.org/>
        prefix owl: <http://www.w3.org/2002/07/owl#>
        prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        prefix xml: <http://www.w3.org/XML/1998/namespace>
        prefix xsd: <http://www.w3.org/2001/XMLSchema#>
        prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix vcard: <http://www.w3.org/2006/vcard/ns#>

        select distinct ?course ?label ?comment ?price ?provider ?title ?skills ?ratings ?reviews ?level ?type ?duration
        where {{
        ?course :price ?price ;
                :course_by ?provider ;
                :title ?title;
                :skills ?skills ;
                :ratings ?ratings ;
                :reviews ?reviews ;
                :level ?level ;
                :type ?type ;
                :duration ?duration .

        ?provider :name ?provider_name .

        filter(contains(lcase(?price), lcase("{price}")))
        SERVICE <https://dbpedia.org/sparql> {{
            OPTIONAl {{
            ?provider rdfs:label ?label ;
                        rdfs:comment ?comment .
            FILTER(LANG(?label) = "en")
            FILTER(LANG(?comment) = "en")
            }}
        }}
        }}
        """
        self.sparql.setQuery(query)
        return self.sparql.queryAndConvert()["results"]["bindings"]
    
    def search_by_skills(self, skill):
        # Query for retrieving course by provider
        query = f"""
        prefix : <https://www.coursera.org/>
        prefix owl: <http://www.w3.org/2002/07/owl#>
        prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        prefix xml: <http://www.w3.org/XML/1998/namespace>
        prefix xsd: <http://www.w3.org/2001/XMLSchema#>
        prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix vcard: <http://www.w3.org/2006/vcard/ns#>

        select distinct ?course ?label ?comment ?price ?provider ?title ?skills ?ratings ?reviews ?level ?type ?duration
        where {{
        ?course :price ?price ;
                :course_by ?provider ;
                :title ?title;
                :skills ?skills ;
                :ratings ?ratings ;
                :reviews ?reviews ;
                :level ?level ;
                :type ?type ;
                :duration ?duration .

        ?provider :name ?provider_name .

        filter(contains(lcase(?skill), lcase("{skill}")))
        SERVICE <https://dbpedia.org/sparql> {{
            OPTIONAl {{
            ?provider rdfs:label ?label ;
                        rdfs:comment ?comment .
            FILTER(LANG(?label) = "en")
            FILTER(LANG(?comment) = "en")
            }}
        }}
        }}
        """
        self.sparql.setQuery(query)
        return self.sparql.queryAndConvert()["results"]["bindings"]
    
    def search_by_ratings(self, ratings):
        # Query for retrieving course by provider
        query = f"""
        prefix : <https://www.coursera.org/>
        prefix owl: <http://www.w3.org/2002/07/owl#>
        prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        prefix xml: <http://www.w3.org/XML/1998/namespace>
        prefix xsd: <http://www.w3.org/2001/XMLSchema#>
        prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix vcard: <http://www.w3.org/2006/vcard/ns#>

        select distinct ?course ?label ?comment ?price ?provider ?title ?skills ?ratings ?reviews ?level ?type ?duration
        where {{
        ?course :price ?price ;
                :course_by ?provider ;
                :title ?title;
                :skills ?skills ;
                :ratings ?ratings ;
                :reviews ?reviews ;
                :level ?level ;
                :type ?type ;
                :duration ?duration .

        ?provider :name ?provider_name .

        filter(?ratings >= {ratings})
        SERVICE <https://dbpedia.org/sparql> {{
            OPTIONAl {{
            ?provider rdfs:label ?label ;
                        rdfs:comment ?comment .
            FILTER(LANG(?label) = "en")
            FILTER(LANG(?comment) = "en")
            }}
        }}
        }}
        """
        self.sparql.setQuery(query)
        return self.sparql.queryAndConvert()["results"]["bindings"]
    
    def search_by_level(self, level):
        # Query for retrieving course by provider
        query = f"""
        prefix : <https://www.coursera.org/>
        prefix owl: <http://www.w3.org/2002/07/owl#>
        prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        prefix xml: <http://www.w3.org/XML/1998/namespace>
        prefix xsd: <http://www.w3.org/2001/XMLSchema#>
        prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix vcard: <http://www.w3.org/2006/vcard/ns#>

        select distinct ?course ?label ?comment ?price ?provider ?title ?skills ?ratings ?reviews ?level ?type ?duration
        where {{
        ?course :price ?price ;
                :course_by ?provider ;
                :title ?title;
                :skills ?skills ;
                :ratings ?ratings ;
                :reviews ?reviews ;
                :level ?level ;
                :type ?type ;
                :duration ?duration .

        ?provider :name ?provider_name .

        filter(contains(lcase(?level), lcase("{level}")))
        SERVICE <https://dbpedia.org/sparql> {{
            OPTIONAl {{
            ?provider rdfs:label ?label ;
                        rdfs:comment ?comment .
            FILTER(LANG(?label) = "en")
            FILTER(LANG(?comment) = "en")
            }}
        }}
        }}
        """
        self.sparql.setQuery(query)
        return self.sparql.queryAndConvert()["results"]["bindings"]
    
    def search_by_type(self, type):
        # Query for retrieving course by provider
        query = f"""
        prefix : <https://www.coursera.org/>
        prefix owl: <http://www.w3.org/2002/07/owl#>
        prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        prefix xml: <http://www.w3.org/XML/1998/namespace>
        prefix xsd: <http://www.w3.org/2001/XMLSchema#>
        prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix vcard: <http://www.w3.org/2006/vcard/ns#>

        select distinct ?course ?label ?comment ?price ?provider ?title ?skills ?ratings ?reviews ?level ?type ?duration
        where {{
        ?course :price ?price ;
                :course_by ?provider ;
                :title ?title;
                :skills ?skills ;
                :ratings ?ratings ;
                :reviews ?reviews ;
                :level ?level ;
                :type ?type ;
                :duration ?duration .

        ?provider :name ?provider_name .

        filter(contains(lcase(?type), lcase("{type}")))
        SERVICE <https://dbpedia.org/sparql> {{
            OPTIONAl {{
            ?provider rdfs:label ?label ;
                        rdfs:comment ?comment .
            FILTER(LANG(?label) = "en")
            FILTER(LANG(?comment) = "en")
            }}
        }}
        }}
        """
        self.sparql.setQuery(query)
        return self.sparql.queryAndConvert()["results"]["bindings"]
