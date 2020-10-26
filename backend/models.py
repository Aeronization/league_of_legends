from django.db import models
import requests
import json

from .constants import (
    LOL_VERSION_URL,
    CHAMPION_PRE_URL,
    CHAMPION_POST_URL,
    SPECIFIC_CHAMPION_POST_URL,
    CHAMPION_SPLASH_URL
)

# (R. Friel - October 21, 2020) - Models are created based on this URL
# and available champion information.
# URL: http://ddragon.leagueoflegends.com/cdn/10.21.1/data/en_US/champion.json
# Check the vesion number.

class Champion(models.Model):
    key = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=255, default=None, primary_key=True)
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

    # Mana/Energy
    mana = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


    @classmethod
    def get_current_lol_version(cls) -> str:
        """
        (R. Friel - October 23, 2020)
        Adhere to single responsibility principle.
        Will return the current patch version of league of legends.

        Returns:
            [str]: The current lol version.
        """
        url = LOL_VERSION_URL

        # (R. Friel - October 23, 2020) - Will return the json response of the current version.
        response: bytes = requests.get(url)
        versions: list = json.loads(response.content)
        current_version: str = str(versions[0])

        return current_version


    @classmethod
    def get_generic_champion_info_url(cls) -> str:
        """
        (R. Friel - October 23, 2020)
        Adhere to single responsibility principle.
        Will return the generic_champion_info url.


        Returns:
            [str]: generic champion info url.
        """
        current_version: str = cls.get_current_lol_version()
        url: str = f"{CHAMPION_PRE_URL}{current_version}{CHAMPION_POST_URL}"

        return url


    @classmethod
    def get_generic_champion_info(cls) -> list:
        """
        (R. Friel - October 23, 2020)
        Adhere to single responsibility principle.
        Fetches and returns the content found from the url.

        Returns:
            list: A list of champion data from each champion.
        """
        url: str = cls.get_generic_champion_info_url()
        response = requests.get(url)
        content: list = json.loads(response.content)

        return content


    @classmethod
    def get_specific_champion_info(cls, champion_name) -> list:
        """
        (R. Friel - October 23, 2020)
        Adhere to single responsibility principle.
        Will return information about a specific champion.

        Returns:
            list: Information about a specific champion.
        """

        current_version: str = cls.get_current_lol_version()
        url: str = f"{CHAMPION_PRE_URL}{current_version}{SPECIFIC_CHAMPION_POST_URL}{champion_name}.json"
        response = requests.get(url)
        content: list = json.loads(response.content)
        content = content["data"][champion_name]

        return content


    @classmethod
    def add_or_update_champions(cls):
        """
        (R. Friel - October 23, 2020)
        Will add new champions, and update all champions with new values.
        """
        all_champions_content: list = cls.get_generic_champion_info()

        for champion_content in all_champions_content["data"]:

            key = champion_content["key"]
            name = champion_content["name"]
            title = champion_content["title"]
            description = champion_content["blurb"]
            info_attack = champion_content["info"]["attack"]
            info_defense = champion_content["info"]["defense"]
            info_magic = champion_content["info"]["magic"]
            info_difficulty = champion_content["info"]["difficulty"]
            mana = champion_content["partype"]
            stats_hp = champion_content["stats"]["hp"]
            stats_hp_per_level = champion_content["stats"]["hpperlevel"]
            stats_mp = champion_content["stats"]["mp"]
            stats_mp_per_level = champion_content["stats"]["mpperlevel"]
            stats_movespeed = champion_content["stats"]["movespeed"]
            stats_armor = champion_content["stats"]["armor"]
            stats_armor_per_level = champion_content["stats"]["armorperlevel"]
            stats_magic_resist = champion_content["stats"]["spellblock"]
            stats_magic_resist_per_level = champion_content["stats"]["spellblockperlevel"]
            stats_attack_range = champion_content["stats"]["attackrange"]
            stats_hp_regen = champion_content["stats"]["hpregen"]
            stats_hp_regen_per_level = champion_content["stats"]["hpregenperlevel"]
            stats_mp_regen = champion_content["stats"]["mpregen"]
            stats_mp_regen_per_level = champion_content["stats"]["mpregenperlevel"]
            stats_crit = champion_content["stats"]["crit"]
            stats_crit_per_level = champion_content["stats"]["critperlevel"]
            stats_attack_damage = champion_content["stats"]["attackdamage"]
            stats_attack_damage_per_level = champion_content["stats"]["attackdamageperlevel"]
            stats_attack_speed = champion_content["stats"]["attackspeed"]
            stats_attack_speed_per_level = champion_content["stats"]["attackspeedperlevel"]

            found_champion = cls.objects.filter(name=name)
            if found_champion:
                found_object.update(
                    key=key,
                    name=name,
                    title=title,
                    description=description,
                    info_attack=info_attack,
                    info_defense=info_defense,
                    info_magic=info_magic,
                    info_difficulty=info_difficulty,
                    mana=mana,
                    stats_hp=stats_hp,
                    stats_hp_per_level=stats_hp_per_level,
                    stats_mp=stats_mp,
                    stats_mp_per_level=stats_mp_per_level,
                    stats_movespeed=stats_movespeed,
                    stats_armor=stats_armor,
                    stats_armor_per_level=stats_armor_per_level,
                    stats_magic_resist=stats_magic_resist,
                    stats_magic_resist_per_level=stats_magic_resist_per_level,
                    stats_attack_range=stats_attack_range,
                    stats_hp_regen=stats_hp_regen,
                    stats_hp_regen_per_level=stats_hp_regen_per_level,
                    stats_mp_regen=stats_mp_regen,
                    stats_mp_regen_per_level=stats_mp_regen_per_level,
                    stats_crit=stats_crit,
                    stats_crit_per_level=stats_crit_per_level,
                    stats_attack_damage=stats_attack_damage,
                    stats_attack_damage_per_level=stats_attack_damage_per_level,
                    stats_attack_speed=stats_attack_speed,
                    stats_attack_speed_per_level=stats_attack_speed_per_level
                )
            else:
                found_object = cls.objects.create(
                    key=key,
                    name=name,
                    title=title,
                    description=description,
                    info_attack=info_attack,
                    info_defense=info_defense,
                    info_magic=info_magic,
                    info_difficulty=info_difficulty,
                    mana=mana,
                    stats_hp=stats_hp,
                    stats_hp_per_level=stats_hp_per_level,
                    stats_mp=stats_mp,
                    stats_mp_per_level=stats_mp_per_level,
                    stats_movespeed=stats_movespeed,
                    stats_armor=stats_armor,
                    stats_armor_per_level=stats_armor_per_level,
                    stats_magic_resist=stats_magic_resist,
                    stats_magic_resist_per_level=stats_magic_resist_per_level,
                    stats_attack_range=stats_attack_range,
                    stats_hp_regen=stats_hp_regen,
                    stats_hp_regen_per_level=stats_hp_regen_per_level,
                    stats_mp_regen=stats_mp_regen,
                    stats_mp_regen_per_level=stats_mp_regen_per_level,
                    stats_crit=stats_crit,
                    stats_crit_per_level=stats_crit_per_level,
                    stats_attack_damage=stats_attack_damage,
                    stats_attack_damage_per_level=stats_attack_damage_per_level,
                    stats_attack_speed=stats_attack_speed,
                    stats_attack_speed_per_level=stats_attack_speed_per_level
                )


    @classmethod
    def process_specific_champion(cls, champion_name):
        """
        (R. Friel - October 23, 2020)
        Will add new champions, and update specific champion with new values.
        The Description will be updated with new Lore.
        Will also create the Skins, Spells, & Passives here.
        """
        champion_content: list = cls.get_specific_champion_info(champion_name)

        key = champion_content["key"]
        name = champion_content["name"]
        title = champion_content["title"]
        description = champion_content["lore"]
        info_attack = champion_content["info"]["attack"]
        info_defense = champion_content["info"]["defense"]
        info_magic = champion_content["info"]["magic"]
        info_difficulty = champion_content["info"]["difficulty"]
        mana = champion_content["partype"]
        stats_hp = champion_content["stats"]["hp"]
        stats_hp_per_level = champion_content["stats"]["hpperlevel"]
        stats_mp = champion_content["stats"]["mp"]
        stats_mp_per_level = champion_content["stats"]["mpperlevel"]
        stats_movespeed = champion_content["stats"]["movespeed"]
        stats_armor = champion_content["stats"]["armor"]
        stats_armor_per_level = champion_content["stats"]["armorperlevel"]
        stats_magic_resist = champion_content["stats"]["spellblock"]
        stats_magic_resist_per_level = champion_content["stats"]["spellblockperlevel"]
        stats_attack_range = champion_content["stats"]["attackrange"]
        stats_hp_regen = champion_content["stats"]["hpregen"]
        stats_hp_regen_per_level = champion_content["stats"]["hpregenperlevel"]
        stats_mp_regen = champion_content["stats"]["mpregen"]
        stats_mp_regen_per_level = champion_content["stats"]["mpregenperlevel"]
        stats_crit = champion_content["stats"]["crit"]
        stats_crit_per_level = champion_content["stats"]["critperlevel"]
        stats_attack_damage = champion_content["stats"]["attackdamage"]
        stats_attack_damage_per_level = champion_content["stats"]["attackdamageperlevel"]
        stats_attack_speed = champion_content["stats"]["attackspeed"]
        stats_attack_speed_per_level = champion_content["stats"]["attackspeedperlevel"]

        # (R. Friel - October 23, 2020) - Create the champion with specific details.
        found_champion = cls.objects.filter(name=name)
        if found_champion:
            found_champion.update(
                key=key,
                name=name,
                title=title,
                description=description,
                info_attack=info_attack,
                info_defense=info_defense,
                info_magic=info_magic,
                info_difficulty=info_difficulty,
                mana=mana,
                stats_hp=stats_hp,
                stats_hp_per_level=stats_hp_per_level,
                stats_mp=stats_mp,
                stats_mp_per_level=stats_mp_per_level,
                stats_movespeed=stats_movespeed,
                stats_armor=stats_armor,
                stats_armor_per_level=stats_armor_per_level,
                stats_magic_resist=stats_magic_resist,
                stats_magic_resist_per_level=stats_magic_resist_per_level,
                stats_attack_range=stats_attack_range,
                stats_hp_regen=stats_hp_regen,
                stats_hp_regen_per_level=stats_hp_regen_per_level,
                stats_mp_regen=stats_mp_regen,
                stats_mp_regen_per_level=stats_mp_regen_per_level,
                stats_crit=stats_crit,
                stats_crit_per_level=stats_crit_per_level,
                stats_attack_damage=stats_attack_damage,
                stats_attack_damage_per_level=stats_attack_damage_per_level,
                stats_attack_speed=stats_attack_speed,
                stats_attack_speed_per_level=stats_attack_speed_per_level
            )
            found_champion=found_champion[0]
        else:
            found_champion = cls.objects.create(
                key=key,
                name=name,
                title=title,
                description=description,
                info_attack=info_attack,
                info_defense=info_defense,
                info_magic=info_magic,
                info_difficulty=info_difficulty,
                mana=mana,
                stats_hp=stats_hp,
                stats_hp_per_level=stats_hp_per_level,
                stats_mp=stats_mp,
                stats_mp_per_level=stats_mp_per_level,
                stats_movespeed=stats_movespeed,
                stats_armor=stats_armor,
                stats_armor_per_level=stats_armor_per_level,
                stats_magic_resist=stats_magic_resist,
                stats_magic_resist_per_level=stats_magic_resist_per_level,
                stats_attack_range=stats_attack_range,
                stats_hp_regen=stats_hp_regen,
                stats_hp_regen_per_level=stats_hp_regen_per_level,
                stats_mp_regen=stats_mp_regen,
                stats_mp_regen_per_level=stats_mp_regen_per_level,
                stats_crit=stats_crit,
                stats_crit_per_level=stats_crit_per_level,
                stats_attack_damage=stats_attack_damage,
                stats_attack_damage_per_level=stats_attack_damage_per_level,
                stats_attack_speed=stats_attack_speed,
                stats_attack_speed_per_level=stats_attack_speed_per_level
            )

        # (R. Friel - October 23, 2020) - Create the champion skins and add relationship to the found_champion.
        skins: list = champion_content["skins"]
        for skin in skins:
            skin_number = str(skin["num"])
            skin_name = skin["name"]
            found_skin_url = f"{CHAMPION_SPLASH_URL}{name}_{skin_number}.jpg"
            found_skin = ChampionSkin.objects.filter(champion=found_champion, name=skin_name)
            if found_skin:
                found_skin.update(image=found_skin_url, name=skin_name)
            else:
                found_skin = ChampionSkin.objects.create(image=found_skin_url, champion=found_champion, name=skin_name)


    @classmethod
    def process_all_champions_specific(cls):
        """
        (R. Friel - October 23, 2020)
        Will get all of the current champions.
        Then process them specifically to get all possible information.
        """
        general_content: list = cls.get_generic_champion_info()
        for champion in general_content["data"]:
            cls.process_specific_champion(champion)

class ChampionSkin(models.Model):
    image = models.ImageField(upload_to="images/", height_field=None, width_field=None, max_length=None, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    champion = models.ForeignKey(Champion, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

# class Ability(models.Model):
