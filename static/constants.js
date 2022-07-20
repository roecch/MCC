const all_players = ['5up', 'antfrost', 'asnazum', 'awesamdude', 'badboyhalo',
  'bbpaws', 'bitzel', 'captainpuffy', 'captainsparklez', 'connoreatspants',
  'cubfan135', 'cxlvxn', 'dantdm', 'dethridge', 'dream', 'drgluon', 'elainaexe',
  'eret', 'f1nn5ter', 'falsesymmetry', 'florianfluke',
  'fruitberries', 'fundy', 'fwhip', 'geenelly', 'geminitay', 'georgenotfound',
  'gizzygazza', 'goodtimeswithscar', 'grain', 'graser10',
  'hbomb94', 'ihascupquake', 'iicbunnyx', 'ijevin', 'illumina',
  'inthelittlewood', 'iskall85', 'itsjustoriah', 'jackmanifold',
  'jacksucksatlife', 'jamescharles', 'jameskii', 'jamesturner', 'jcthecaster',
  'jeromeasf', 'jestanii', 'joeygraceffa', 'karacorvus',
  'karljacobs', 'katherineelizabeth', 'kingburren', 'kontuz', 'krinios',
  'krtzzy', 'kryticzeuz', 'laurenzside', 'ldshadowlady', 'ludwig',
  'marielitai', 'mefs', 'michaelmcchill', 'minimuka', 'nettyplays', 'nihachu',
  'pearlbytez', 'pearlescentmoon', 'petezahhut', 'philza',
  'plumbella', 'pokimane', 'ponk', 'prestonplayz', 'punz', 'purpled',
  'quackity', 'quig', 'rafessor', 'ranboo', 'rendog', 'ripmika',
  'roguskii', 'rtgame', 'ryguyrocky', 'sapnap', 'sb737', 'scotgrisworld',
  'seapeekay', 'shubble', 'skeppy', 'slimecicle', 'smajor1995',
  'smallishbeans', 'sneegsnag', 'solidaritygaming', 'spifey', 'steph0sims',
  'strawburry17', 'sylvee', 'tankmatt', 'tapl', 'technoblade',
  'theorionsound', 'tommyinnit', 'toxxicsupport', 'tubbo', 'vapekit', 'vgumiho',
  'vikkstar123', 'vixella', 'voiceoverpete', 'wilbur',
  'wisp', 'wolv21', 'yammyxox', 'yeetdaisie'];

function getPlayerImgMap()
{
  let map = new Map();
  fetch("/static/list_of_images.json")
  .then(response => {
     return response.json();
  })
  .then(jsondata => {
    let data = JSON.stringify(jsondata);
    data = data.replaceAll("\"", '');
    data = data.replaceAll('"', '');
    data = data.replaceAll("{", '');
    data = data.replaceAll("}", '');
    let lines = data.split(",");

    lines.forEach(function(line) {
      map.set(line.substr(0, line.indexOf(':')), line.substr(line.indexOf(':') + 1))
    });
  });
  console.log(map)
  return map;
}