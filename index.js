const dotenv = require('dotenv');
dotenv.config();
(async()=>{
    // default imports
    const events = require('events');
    const { exec } = require("child_process")
    const logs = require("discord-logs")
    const Discord = require("discord.js")
    const { 
        MessageEmbed, 
        MessageButton, 
        MessageActionRow, 
        Intents, 
        Permissions, 
        MessageSelectMenu 
    }= require("discord.js")
    const fs = require('fs');
    let process = require('process');
    const delay = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

    // block imports
    let https = require("https")
    const Database  = require("easy-json-database")
    
    // define s4d components (pretty sure 90% of these arnt even used/required)
    let s4d = {
        Discord,
        fire:null,
        joiningMember:null,
        reply:null,
        player:null,
        manager:null,
        Inviter:null,
        message:null,
        notifer:null,
        checkMessageExists() {
            if (!s4d.client) throw new Error('You cannot perform message operations without a Discord.js client')
            if (!s4d.client.readyTimestamp) throw new Error('You cannot perform message operations while the bot is not connected to the Discord API')
        }
    };

    // check if d.js is v13
    if (!require('./package.json').dependencies['discord.js'].startsWith("^13.")) {
      let file = JSON.parse(fs.readFileSync('package.json'))
      file.dependencies['discord.js'] = '^13.16.0'
      fs.writeFileSync('package.json', JSON.stringify(file, null, 4))
      exec('npm i')
      throw new Error("Seems you arent using v13 please re-run or run `npm i discord.js@13.16.0`");
    }

    // check if discord-logs is v2
    if (!require('./package.json').dependencies['discord-logs'].startsWith("^2.")) {
      let file = JSON.parse(fs.readFileSync('package.json'))
      file.dependencies['discord-logs'] = '^2.0.0'
      fs.writeFileSync('package.json', JSON.stringify(file, null, 4))
      exec('npm i')
      throw new Error("discord-logs must be 2.0.0. please re-run or if that fails run `npm i discord-logs@2.0.0` then re-run");
    }

    // create a new discord client
    s4d.client = new s4d.Discord.Client({
        intents: [
            Object.values(s4d.Discord.Intents.FLAGS).reduce((acc, p) => acc | p, 0)
        ],
        partials: [
            "REACTION", 
            "CHANNEL"
        ]
    });

    // when the bot is connected say so
    s4d.client.on('ready', () => {
        console.log(s4d.client.user.tag + " is alive!")
    })

    // upon error print "Error!" and the error
    process.on('uncaughtException', function (err) {
        console.log('Error!');
        console.log(err);
    });

    // give the new client to discord-logs
    logs(s4d.client);

    // pre blockly code
    

    // blockly code
    await s4d.client.login(process.env.DISCORD_TOKEN).catch((e) => {
            const tokenInvalid = true;
            const tokenError = e;
            if (e.toString().toLowerCase().includes("token")) {
                throw new Error("An invalid bot token was provided!")
            } else {
                throw new Error("Privileged Gateway Intents are not enabled! Please go to https://discord.com/developers and turn on all of them.")
            }
        });
    
    const database1 = new Database('./database.json')
    s4d.client.on('interactionCreate', async (interaction) => {
              if ((interaction.commandName) == 'add') {
        database1.add(String('count'), parseInt(1));
        await interaction.reply({ content: ('added 1 database, currently at: ' + String(database1.get(String('count')))), ephemeral: true, components: [] });
      }
    
        });
    
    s4d.client.on('interactionCreate', async (interaction) => {
              if ((interaction.commandName) == 'subtract') {
        database1.subtract(String('count'), parseInt(1));
        await interaction.reply({ content: ('subtracted 1 database, currently at: ' + String(database1.get(String('count')))), ephemeral: true, components: [] });
      }
    
        });
    
    s4d.client.on('interactionCreate', async (interaction) => {
              if ((interaction.commandName) == 'reset') {
        database1.delete(String('count'));
        await interaction.reply({ content: 'reset database', ephemeral: true, components: [] });
      }
    
        });
    
    s4d.client.on('interactionCreate', async (interaction) => {
              if ((interaction.commandName) == 'verify') {
        (interaction.member).roles.add(((s4d.client.guilds.cache.get('1012562113069318164')).roles.cache.get('1012571734337142824')));
      }
    
        });
    
    s4d.client.on('interactionCreate', async (interaction) => {
              if ((interaction.commandName) == 'purge') {
        (interaction.channel).bulkDelete(((interaction.options.getInteger('amount'))|1));
      }
    
        });
    
    return s4d
})();
        });
    
    return s4d
})();
