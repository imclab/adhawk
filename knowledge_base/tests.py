"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from knowledge_base.models import Market,MediaType,Source

#class AdModelTest(TestCase):
#    def test_creating_a_new_Ad_and_saving_it_to_the_database(self):
#        # TODO: Create a new Ad object 
#        self.fail('todo: finish '+self.id())
#
#class AuthorModelTest(TestCase):
#    def test_creating_a_new_Author_and_saving_it_to_the_database(self):
#        # TODO: Create a new Author object 
#        self.fail('todo: finish '+self.id())
#
#class BroadcastTypeModelTest(TestCase):
#    def test_creating_a_new_BroadcastType_and_saving_it_to_the_database(self):
#        # TODO: Create a new BroadcastType object 
#        self.fail('todo: finish '+self.id())
#
#class CandidateModelTest(TestCase):
#    def test_creating_a_new_Candidate_and_saving_it_to_the_database(self):
#        # TODO: Create a new Candidate object 
#        self.fail('todo: finish '+self.id())
#
#class CandidateStatusModelTest(TestCase):
#    def test_creating_a_new_CandidateStatus_and_saving_it_to_the_database(self):
#        # TODO: Create a new CandidateStatus object 
#        self.fail('todo: finish '+self.id())
#
#class CommitteeDesignationModelTest(TestCase):
#    def test_creating_a_new_CommitteeDesignation_and_saving_it_to_the_database(self):
#        # TODO: Create a new CommitteeDesignation object 
#        self.fail('todo: finish '+self.id())
#
#class CommitteeTypeModelTest(TestCase):
#    def test_creating_a_new_CommitteeType_and_saving_it_to_the_database(self):
#        # TODO: Create a new CommitteeType object 
#        self.fail('todo: finish '+self.id())
#     
#class ConnectedOrganizationModelTest(TestCase):
#    def test_creating_a_new_ConnectedOrganization_and_saving_it_to_the_database(self):
#        # TODO: Create a new ConnectedOrganization object 
#        self.fail('todo: finish '+self.id())
#
#class CoverageModelTest(TestCase):
#    def test_creating_a_new_Coverage_and_saving_it_to_the_database(self):
#        # TODO: Create a new Coverage object 
#        self.fail('todo: finish '+self.id())
#
#class CoverageTypeModelTest(TestCase):
#    def test_creating_a_new_CoverageType_and_saving_it_to_the_database(self):
#        # TODO: Create a new CoverageType object 
#        self.fail('todo: finish '+self.id())
#        
#class FunderModelTest(TestCase):
#    def test_creating_a_new_Funder_and_saving_it_to_the_database(self):
#        # TODO: Create a new CommitteeDesignation object 
#        self.fail('todo: finish '+self.id())
#
#class IncumbentChallengerStatusModelTest(TestCase):
#    def test_creating_a_new_IncumbentChallengerStatus_and_saving_it_to_the_database(self):
#        # TODO: Create a new IncumbentChallengerStatus object 
#        self.fail('todo: finish '+self.id())
#
#class InterestGroupCategoryModelTest(TestCase):
#    def test_creating_a_new_InterestGroupCategory_and_saving_it_to_the_database(self):
#        # TODO: Create a new InterestGroupCategory object 
#        self.fail('todo: finish '+self.id())
#
#class IssueModelTest(TestCase):
#    def test_creating_a_new_Issue_and_saving_it_to_the_database(self):
#        # TODO: Create a new Issue object 
#        self.fail('todo: finish '+self.id())
#
#class IssueCategoryModelTest(TestCase):
#    def test_creating_a_new_IssueCategory_and_saving_it_to_the_database(self):
#        # TODO: Create a new IssueCategory object 
#        self.fail('todo: finish '+self.id())
#
class MarketModelTest(TestCase):
    def test_creating_a_new_Market_and_saving_it_to_the_database(self):
        # create a new Market object
        market = Market()
        market.market_type = 'A'
        market.name = 'New New York'

        # check that we can save it
        market.save()

        # check that we can find it
        all_markets_in_database = Market.objects.all()
        self.assertEquals(len(all_markets_in_database),1)
        only_market_in_database = all_markets_in_database[0]
        self.assertEquals(only_market_in_database, market)

        # check that its attributes have been saved
        self.assertEquals(only_market_in_database.market_type,"A")
        self.assertEquals(only_market_in_database.name, "New New York")



#class MediaModelTest(TestCase):
#    def test_creating_a_new_Media_and_saving_it_to_the_database(self):
#        # TODO: Create a new Media object 
#        self.fail('todo: finish '+self.id())
#
#class MediaProfileModelTest(TestCase):
#    def test_creating_a_new_MediaProfile_and_saving_it_to_the_database(self):
#        # TODO: Create a new MediaProfile object 
#        self.fail('todo: finish '+self.id())

class MediaTypeModelTest(TestCase):
    def test_creating_a_new_MediaType_and_saving_it_to_the_database(self):
        # create a new MediaType
        media_type = MediaType()
        media_type.main_url = "http://www.youtube.com"
        media_type.scraper_added = True
        
        # check that we can save it
        media_type.save()

        # check that we can find it
        all_media_types_in_database = MediaType.objects.all()
        self.assertEquals(len(all_media_types_in_database),1)
        only_media_type_in_database = all_media_types_in_database[0]
        self.assertEquals(only_media_type_in_database, media_type)

        # check that its attributes have been saved
        self.assertEquals(only_media_type_in_database.main_url,
        "http://www.youtube.com")
        self.assertEquals(only_media_type_in_database.scraper_added, True)
    def test_creating_a_new_MediaType_with_default_values(self):
        # create a new MediaType, not specifying defaulted fields
        media_type = MediaType()
        media_type.main_url = "http://www.youtube.com"
        
        # assert that defaults are correct
        self.assertEquals(media_type.scraper_added,False)

class SourceModelTest(TestCase):
    def test_creating_a_new_Source_and_saving_it_to_the_database(self):
        # create a new Source
        source = Source()
        source.main_url = "http://www.factcheck.org"
        source.scraper_added = True
        
        # check that we can save it
        source.save()

        # check that we can find it
        all_sources_in_database = Source.objects.all()
        self.assertEquals(len(all_sources_in_database),1)
        only_source_in_database = all_sources_in_database[0]
        self.assertEquals(only_source_in_database, source)

        # check that its attributes have been saved
        self.assertEquals(only_source_in_database.main_url,
        "http://www.factcheck.org")
        self.assertEquals(only_source_in_database.scraper_added, True)
    def test_creating_a_new_Source_with_default_values(self):
        # create a new MediaType, not specifying defaulted fields
        source = Source()
        source.main_url = "http://www.youtube.com"
        
        # assert that defaults are correct
        self.assertEquals(source.scraper_added,False)

#class StanceModelTest(TestCase):
#    def test_creating_a_new_Stance_and_saving_it_to_the_database(self):
#        # TODO: Create a new Stance object 
#        self.fail('todo: finish '+self.id())
#
#class TagModelTest(TestCase):
#    def test_creating_a_new_Tag_and_saving_it_to_the_database(self):
#        # TODO: Create a new Tag object 
#        self.fail('todo: finish '+self.id())
#
