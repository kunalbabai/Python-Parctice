import random

#story time 
enemy = random.choice (["chihuahua", "border collie", "wolf","God of Mischief","Icarus","Crate","Big Tex","Winter Jack","Sandman","Megatron","Joker","Ganon","Serpentor","Thanos","Magneto","Doctor Doom"])
father = random.choice (["John", "Mr.Pickles", "Hairyface", "Willy Wonka", "Steve", "Bob","Alfred","Allan","Abraham","Andrew","Bailey","Clyde","Fernando","Francis","Elias","Gerrit","Jacob","Morris","Winton"])
enemyadj = ["grimy", "muddy", "awful", "grotesque", "hideous", "adorable", "cute","grotty","scungy","dusty","filthy","nasty","dreadful","horrible","egregious","pathetic","abysmal","horrendous","horrific"]

intro1 = "I was sitting on the edge of the rocky cliff beside my favourite tree."
intro2 = "Alone in the searing desert, I was wondering why I was leaning against a cactus."
intro3 = "Staring out my apartment window, I saw my reflection staring back at me."
intro4 = "I saw something in the distance, or rather someone."


char1 = "As I looked out into the distance, I thought about my past and all of the drama in it."
char2 = "I wondered if this was my destiny- trying to find happiness."
char3 = "I pulled out the photo of my long lost mother and where on earth she could be."


prob1 = "Suddenly I was covered from head to toe with darkness. I couldn't breathe or see. Everything went black..."
prob2 = "All of a sudden a psychopathic " + enemy + " grinned at me,showing all his razor sharp teeth. Suddenly it started to claw at my face. From the loss of blood, I collapsed onto the tough ground..."
prob3 = "I suddenly felt a sharp needle sink into my flesh. It was a tranquilizer. But before I knew it I started feeling really drowsy. Everything went black..."


sol1 = "I forced my drowsy eyes open my eyes to see a bright light."
sol2 = "I forced my drowsy eyes open to find myself on the back of a massive dragon and a man in front of me."
sol3 = "I forced my drowsy eyes open to the sounds of a " + random.choice(enemyadj) + " " +enemy + " licking my face."


end1 = "A man came to my side with a knife. It was my father!" + father + "!" "'Go to sleep young one...'"
end2 = "It was difficult to keep my eyes open as I struggled to breathe. "
end3 = "Out of nowhere, a duck wearing a deerstalker looked me in the eye and pointed a gun at me. 'Quack.' And that was the last thing I heard..."
 
intros = [intro1, intro2, intro3, intro4]
characters = [char1, char2, char3]
problems = [prob1, prob2, prob3]
solutions = [sol1, sol2, sol3]
endings = [end1, end2, end3]
def story_Generator(intros,characters,problems,solutions,endings):
    try:
        return random.choice(intros)+ ','+random.choice(characters)+','+random.choice(problems)+','+random.choice(solutions)+','+random.choice(endings)
    except Exception as Ex:
        return Ex

strory = story_Generator(intros,characters,problems,solutions,endings)
print(strory)