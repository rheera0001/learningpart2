from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from djongo import models

# Define models for demonstration (in real app, use models.py)
class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)
    class Meta:
        app_label = 'octofit_tracker'

class Activity(models.Model):
    user = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    duration = models.IntegerField()
    team = models.CharField(max_length=100)
    class Meta:
        app_label = 'octofit_tracker'

class Leaderboard(models.Model):
    team = models.CharField(max_length=100)
    points = models.IntegerField()
    class Meta:
        app_label = 'octofit_tracker'

class Workout(models.Model):
    name = models.CharField(max_length=100)
    difficulty = models.CharField(max_length=50)
    class Meta:
        app_label = 'octofit_tracker'

User = get_user_model()

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Clear collections
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Teams
        marvel = Team.objects.create(name='Marvel')
        dc = Team.objects.create(name='DC')

        # Users
        ironman = User.objects.create_user(username='ironman', email='ironman@marvel.com', password='pass')
        batman = User.objects.create_user(username='batman', email='batman@dc.com', password='pass')
        wonderwoman = User.objects.create_user(username='wonderwoman', email='wonderwoman@dc.com', password='pass')
        spiderman = User.objects.create_user(username='spiderman', email='spiderman@marvel.com', password='pass')

        # Activities
        Activity.objects.create(user='ironman', type='run', duration=30, team='Marvel')
        Activity.objects.create(user='batman', type='cycle', duration=45, team='DC')
        Activity.objects.create(user='wonderwoman', type='swim', duration=60, team='DC')
        Activity.objects.create(user='spiderman', type='run', duration=25, team='Marvel')

        # Leaderboard
        Leaderboard.objects.create(team='Marvel', points=55)
        Leaderboard.objects.create(team='DC', points=105)

        # Workouts
        Workout.objects.create(name='Hero HIIT', difficulty='Hard')
        Workout.objects.create(name='Sidekick Cardio', difficulty='Medium')

        self.stdout.write(self.style.SUCCESS('octofit_db populated with test data.'))
