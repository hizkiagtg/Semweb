from rdflib import Graph

class RDFHandle:
    def __init__(self, filename, format):
        self.graph = Graph()
        self.graph.parse(filename, format)

    def search(self, search_by, query):
        if search_by == 'course':
            return self.seach_by_course(query)
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

        select distinct ?course ?price ?provider ?title ?skills ?ratings ?reviews ?level ?type ?duration
        where {{
        ?course :price ?price ;
                :course_by ?provider ;
                :title ?title;
                :skills ?skills ;
                :ratings ?ratings ;
                :level ?level ;
                :type ?type ;
                :duration ?duration .

        filter(contains(lcase(?provider), lcase("{provider}")))
        }}
        """
        result = self.graph.query(query)
        return result
        
    def seach_by_course(self, course):
        # Query for retrieving course by provider
        query = f"""
        prefix : <https://www.coursera.org/>
        prefix owl: <http://www.w3.org/2002/07/owl#>
        prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
        prefix xml: <http://www.w3.org/XML/1998/namespace>
        prefix xsd: <http://www.w3.org/2001/XMLSchema#>
        prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        prefix vcard: <http://www.w3.org/2006/vcard/ns#>

        select distinct ?course ?price ?provider ?title ?skills ?ratings ?reviews ?level ?type ?duration
        where {{
        ?course :price ?price ;
                :course_by ?provider ;
                :title ?title;
                :skills ?skills ;
                :ratings ?ratings ;
                :level ?level ;
                :type ?type ;
                :duration ?duration .

        filter(contains(lcase(?provider), lcase("{course}")))
        }}
        """
        result = self.graph.query(query)
        return result