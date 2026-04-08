from django.core.management.base import BaseCommand
from tracker.models import Team, Activity, Leaderboard, Workout
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        User = get_user_model()
        # Delete existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()

        # Create Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Create Users (superheroes)
        users = [
            User.objects.create_user(username='ironman', email='ironman@marvel.com', password='password', team=marvel),
            User.objects.create_user(username='captainamerica', email='cap@marvel.com', password='password', team=marvel),
            User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='password', team=marvel),
            User.objects.create_user(username='batman', email='batman@dc.com', password='password', team=dc),
            User.objects.create_user(username='superman', email='superman@dc.com', password='password', team=dc),
            User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='password', team=dc),
        ]

        # Create Workouts
        workout1 = Workout.objects.create(name='Pushups', description='Upper body strength')
        workout2 = Workout.objects.create(name='Running', description='Cardio endurance')
        workout3 = Workout.objects.create(name='Squats', description='Lower body strength')

        # Create Activities
        Activity.objects.create(user=users[0], workout=workout1, duration=30)
        Activity.objects.create(user=users[1], workout=workout2, duration=45)
        Activity.objects.create(user=users[2], workout=workout3, duration=20)
        Activity.objects.create(user=users[3], workout=workout1, duration=25)
        Activity.objects.create(user=users[4], workout=workout2, duration=35)
        Activity.objects.create(user=users[5], workout=workout3, duration=40)

        # Create Leaderboard
        Leaderboard.objects.create(user=users[0], score=100)
        Leaderboard.objects.create(user=users[1], score=90)
        Leaderboard.objects.create(user=users[2], score=80)
        Leaderboard.objects.create(user=users[3], score=95)
        Leaderboard.objects.create(user=users[4], score=85)
        Leaderboard.objects.create(user=users[5], score=75)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data.'))
