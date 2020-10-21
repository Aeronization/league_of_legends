from django.db import models

# (R. Friel - October 21, 2020) - Models are created based on this URL
# and available champion information.

# Create your models here.
class Champion(models.Model):
    key = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    # Info
    info_attack = models.IntegerField(null=True, blank=True)
    info_defense = models.IntegerField(null=True, blank=True)
    info_magic = models.IntegerField(null=True, blank=True)
    info_difficulty =models.IntegerField(null=True, blank=True)

    # Stats
    stats_hp = models.FloatField(null=True, blank=True)
    stats_hp_per_level = models.FloatField(null=True, blank=True)
    stats_mp = models.FloatField(null=True, blank=True)
    stats_mp_per_level = models.FloatField(null=True, blank=True)
    stats_movespeed = models.FloatField(null=True, blank=True)
    stats_armor = models.FloatField(null=True, blank=True)
    stats_armor_per_level = models.FloatField(null=True, blank=True)
    stats_magic_resist = models.FloatField(null=True, blank=True)
    stats_magic_resist_per_level = models.FloatField(null=True, blank=True)
    stats_attack_range = models.FloatField(null=True, blank=True)
    stats_hp_regen = models.FloatField(null=True, blank=True)
    stats_hp_regen_per_level = models.FloatField(null=True, blank=True)
    stats_mp_regen = models.FloatField(null=True, blank=True)
    stats_mp_regen_per_level = models.FloatField(null=True, blank=True)
    stats_crit = models.FloatField(null=True, blank=True)
    stats_crit_per_level = models.FloatField(null=True, blank=True)
    stats_attack_damage = models.FloatField(null=True, blank=True)
    stats_attack_damage_per_level = models.FloatField(null=True, blank=True)
    stats_attack_speed = models.FloatField(null=True, blank=True)
    stats_attack_speed_per_level = models.FloatField(null=True, blank=True)

    # Image
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None, null=True, blank=True)

    # Mana/Energy
    mana = models.CharField(max_length=255, null=True, blank=True)
