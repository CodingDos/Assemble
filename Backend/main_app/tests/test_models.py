import logging
from django.test import TestCase
from django.utils import timezone
from django.db.utils import IntegrityError
from main_app.models import Skill, User, Team, Hackathon, Category, Badge

logger = logging.getLogger('main_app')

class SkillTestCase(TestCase): 
    #Will test if the instance of the skill has been added correctly
    def setUp(self):
        self.category = Category.objects.create(name='Languages')
        self.skill = Skill.objects.create(name="Python", category=self.category)
        logger.debug(f"Setup: Created Skill Instance {self.skill.name} from {self.category.name}")  #only used for debugging
    
    def test_skill_category(self):
        self.assertEqual(self.skill.category.name, 'Languages')

    #Will test if the __str__ method in models will be the same name as the instance created
    def test_skill_str(self):
        self.assertEqual(str(self.skill), f"{self.skill.name} ({self.skill.category.name})")



class CategoryTestCase(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Programming Languages")

    def test_category_str(self):
        self.assertEqual(str(self.category), 'Programming Languages')



class BadgeTestCase(TestCase):
    #Will test if the instance of the badge has been added correctly
    def setUp(self):
        self.badge = Badge.objects.create(name="Next.Js", description="Used Next.JS in 3 projects")
        logger.debug(f'Setup: Created Badge Instance {self.badge.name} & Badge Description: {self.badge.description}')    

    #Will test if the __str__ method in models will be the same name as the instance created
    def test_badge_str(self):
        self.assertEqual(str(self.badge), self.badge.name)



class UserTestCase(TestCase):
    def setUp(self):
        #Creates instance of category
        self.category_framework = Category.objects.create(name='Framework')
        self.category_language = Category.objects.create(name='Language')

        #Creates a instance of skills
        self.skill_react = Skill.objects.create(name='React', category=self.category_framework)
        self.skill_java = Skill.objects.create(name='Java', category=self.category_language)

        #Creates the instance of a user
        self.user = User.objects.create_user(
            username ='john doe', 
            email ='johndoe@email.com',
            password ='testpass',
            description ="Passionate Developer",
            linkedIn_url = 'https://www.linkedin.com/in/john-lopez01/',
            github_url = 'https://github.com/JLopez0001',
        )

        self.user.skills.add(self.skill_react, self.skill_java)

    #Test the instance if it was created 
    def test_user_creation(self):
        self.assertEqual(self.user.username, 'john doe')
        self.assertEqual(self.user.email, 'johndoe@email.com')
        self.assertTrue(self.user.check_password('testpass'))
        self.assertEqual(self.user.description, 'Passionate Developer')
        self.assertTrue(self.user.is_active)
        self.assertFalse(self.user.is_staff)

    #Email needs to be unique so this test will test if email is unique
    def test_user_email_is_unique(self):
        with self.assertRaises(IntegrityError):    #function will pass test if there is an error since it expects an error
            User.objects.create(
                username='jane doe',
                email="johndoe@email.com", 
                password='testpass'
    )

    #username needs to be unique so this test will test if username is unique
    def test_user_username_is_unique(self):
        with self.assertRaises(IntegrityError):    #function will pass test if there is an error since it expects an error
            User.objects.create(
                username='john doe',
                email='test@email.com',
                password='testpass'
            )
    
    # Test if the user is able to be enrolled in a team
    def test_user_entering_team(self):
        team = Team.objects.create(team_name="Developer")
        team.members.add(self.user)
        self.assertIn(self.user, team.members.all())
        self.assertEqual(team.members.count(), 1)

    # Test to see if the user skills are added to the user
    def test_user_skills(self):
        skills = self.user.skills.all()
        self.assertIn(self.skill_react, skills)
        self.assertIn(self.skill_java, skills)
        self.assertEqual(self.user.skills.count(), 2)
        
    def test_user_str(self):
        self.assertEqual(str(self.user), self.user.username)



class TeamTestCase(TestCase):
    #Test user creation and the ability to add them to the team with a creation of the team name
    def setUp(self):
        self.user1 = User.objects.create(username='user1', email='user1@email.com', password='testpass')
        self.user2 = User.objects.create(username='user2', email='user2@email.com', password='testpass')
        
        self.team = Team.objects.create(team_name = 'StarFish')
        self.team.members.add(self.user1, self.user2)
    
    #Test the amount of users in the database for members and check if each user is in the team instance as members
    def test_team_members(self):
        members = self.team.members.all() #Saves all members in the test database from the team into a variable

        self.assertEqual(self.team.members.count(), 2)
        self.assertIn(self.user1, members)
        self.assertIn(self.user2, members)
        logger.debug(f'Members: Created members: {self.user1, self.user2} in team: {self.team.team_name}') 

    #Test if the instance name is the same as the value passed for team name
    def test_team_name_str(self):
        self.assertEqual(str(self.team.team_name), 'StarFish')
    


class HackathonTestCase(TestCase):
    def setUp(self):
        # Creates test teams to be added to hackathon
        self.team1 = Team.objects.create(team_name='team1')
        self.team2 = Team.objects.create(team_name='team2')

        # Creates hackathon instance
        self.hackathon = Hackathon.objects.create(
            name="Test Hackathon",
            description="This is a test hackathon",
            logo="https://pngimg.com/uploads/facebook_logos/facebook_logos_PNG19759.png",
            # Create timezone-aware datetime objects
            start_date = timezone.make_aware(timezone.datetime(2024, 8, 1, 10, 0, 0)),
            end_date = timezone.make_aware(timezone.datetime(2024, 8, 3, 10, 0, 0))
        )
        self.hackathon.teams.add(self.team1, self.team2) 
        self.hackathon.team_winner = self.team1
        self.hackathon.save()

    # Test the instance that was created
    def test_hackathon_creation(self):
        self.assertEqual(self.hackathon.name, 'Test Hackathon')
        self.assertEqual(self.hackathon.description, 'This is a test hackathon')
        self.assertEqual(self.hackathon.teams.count(), 2) #Will check if the 2 teams that were created are in the hackathon

    # Test if the teams are in the hackathon
    def test_hackathon_teams(self):
        teams = self.hackathon.teams.all()  #Saves all teams in the test database from the team into a variable

        self.assertIn(self.team1, teams)
        self.assertIn(self.team2, teams)
        self.assertEqual(teams.count(), 2)

    def test_hackathon_winner(self):
        hackathon = Hackathon.objects.get(id=self.hackathon.id)
        self.assertEqual(hackathon.team_winner, self.team1)

        logger.debug(f'Test Winning Team: {hackathon.team_winner.team_name} won the {hackathon.name}')

    def test_hackathon_str(self):
        self.assertEqual(str(self.hackathon), "Test Hackathon")
