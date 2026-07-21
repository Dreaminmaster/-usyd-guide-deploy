// Provenance policy and selected deep-dive enrichments.
DATA.provenancePolicy={
 official:{label:'官方事实',desc:'学校或主管机构明确发布的规则、资格、日期和要求。'},
 system:{label:'官方系统路径',desc:'登录后实际使用的菜单、按钮和操作入口。'},
 community:{label:'学生经验',desc:'学生反复遇到的实际情况，只作补充参考。'},
 editorial:{label:'实操整理',desc:'根据官方信息压缩出的操作顺序、提醒和排查。'}
};
DATA.topicEvidence={
 'card-1':{official:true,system:true,editorial:true},
 'card-2':{official:true,system:true},
 'card-4':{official:true},
 'card-7':{official:true,editorial:true},
 'card-8':{official:true,system:true,editorial:true}
};
(function(){
 const byId=Object.fromEntries(DATA.topics.map(t=>[t.id,t]));
 const card=byId['card-1'];
 if(card){
  card.summary='把数字学生证加入 iPhone 或 Apple Watch，并确认门禁、打印、丢失停用和恢复方式。';
  card.prerequisites=[
   '已经完成 enrolment，UniKey 和 Okta 可以正常登录。',
   '学生证照片已获批；照片审核通常需要几个工作日。',
   'iPhone 已登录 Apple ID，并安装最新版 Transact eAccounts。',
   '需要添加 Apple Watch 时，先完成手表与 iPhone 配对。'
  ];
  card.sections=[
   {title:'添加到 iPhone 或 Apple Watch',sourceKind:'system',items:[
    '打开 Transact eAccounts，选择 University of Sydney，并用 UniKey 与 Okta 登录。',
    '在首页选择 Add to Apple Wallet，先选 iPhone，按提示确认条款并完成添加。',
    '需要手表版本时，再回到 eAccounts 选择 Apple Watch。',
    '最后分别在 iPhone 与手表 Wallet 中确认学生证已经显示。'
   ]},
   {title:'添加后检查',sourceKind:'official',items:[
    '门禁和图书馆权限可能需要约 24 小时同步，打印通常需要 12–24 小时。',
    '先测试 Wallet 能否调出学生证，再测试门禁、图书馆和打印。',
    '数字学生证可用于支持学生证的校园服务，但正式考试仍需实体学生证。',
    '实体卡不会因添加数字卡而自动失效，建议继续随身保留。'
   ]},
   {title:'手机丢失、换机或需要停用',sourceKind:'system',items:[
    '进入 eAccounts → Settings → Card Management，关闭丢失设备对应的凭证。',
    '也可在 SydPay 网页端进入 Card Services，停用指定的手机或手表凭证。',
    '找回设备后，可在相同位置重新启用；换机时先停用旧设备再添加新设备。',
    '只停用被选中的凭证，其他设备和实体卡通常不会同时失效。'
   ]}
  ];
  card.warnings=[
   '数字学生证不能替代正式考试和部分身份核验场景所需的实体学生证。',
   '交通 concession 是否适用要单独确认，不能仅凭 Wallet 中显示学生证判断。',
   '学生证只能本人使用；不要转借、截图伪造或篡改。'
  ];
  card.troubleshooting=[
   '没有 Add to Apple Wallet：先检查 enrolment、照片审批、UniKey、Okta 和设备兼容性。',
   '已经添加但门禁无效：先等待同步，再记录建筑、时间和提示情况后联系学校支持。',
   '打印不能用：检查 SydPay、余额和打印账户，并等待 12–24 小时。',
   '联系支持时准备报错截图、设备型号、iOS 与 eAccounts 版本。'
  ];
  card.editorNotes=[];
 }

 const lost=byId['card-8'];
 if(lost){
  lost.officialPath='eAccounts → Settings → Card Management；或 SydPay → Card Services';
  lost.prerequisites=['先确认丢失的是实体卡、iPhone、Apple Watch，还是多项凭证。','Apple 设备丢失时先使用 Find My 锁定设备。'];
  lost.sections=[
   {title:'立即停用',sourceKind:'system',items:['在 eAccounts 的 Card Management 中关闭对应设备凭证。','无法使用 App 时，在 SydPay 网页端停用指定凭证。','实体卡遗失则单独报告实体卡，不要只停用手机。']},
   {title:'找回或换机',sourceKind:'system',items:['找回设备后在原位置重新启用。','换机时先确保旧设备凭证已停用，再在新设备重新添加。','恢复后重新测试 Wallet、门禁和打印。']}
  ];
  lost.warnings=['只停用被选中的凭证；其他设备和实体卡通常仍可使用。','如发现 SydPay 异常消费或门禁异常，应同时联系对应支持团队。'];
  lost.editorNotes=[];
 }

})();

function evidenceChip(kind){const p=DATA.provenancePolicy[kind];return p?`<span class="evidence-chip ${kind}">${esc(p.label)}</span>`:''}
function evidenceKinds(t){const explicit=DATA.topicEvidence[t.id]||{};const kinds=[];if((t.sourceKeys||[t.source]).some(k=>DATA.sources[k]?.firstParty))kinds.push('official');if(t.officialPath||(t.sections||[]).some(s=>s.sourceKind==='system'))kinds.push('system');if(t.communityNotes?.length||explicit.community)kinds.push('community');if(t.editorNotes?.length||t.troubleshooting?.length||explicit.editorial)kinds.push('editorial');return [...new Set(kinds)]}
function evidenceLegend(){const p=DATA.provenancePolicy;return `<section class="evidence-legend"><h2>来源标识</h2><div class="evidence-grid">${Object.entries(p).map(([k,v])=>`<div class="evidence-item ${k}">${evidenceChip(k)}<b>${esc(v.label)}</b><p>${esc(v.desc)}</p></div>`).join('')}</div></section>`}
function renderHome(){
 const guides=DATA.topics.filter(t=>t.type==='guide').length,faqs=DATA.topics.filter(t=>t.type==='faq').length;
 $('#stats').innerHTML=[[DATA.topics.length,'可搜索条目'],[DATA.editorialGuideCount,'重点操作流程'],[faqs,'常见问题'],[Object.keys(DATA.sources).length,'已核验来源']].map(x=>`<div class="stat"><b>${x[0]}</b><span>${x[1]}</span></div>`).join('');
 $('#homeCategories').innerHTML=DATA.categories.map(c=>`<article class="catcard" data-cat="${c.id}"><div class="caticon">${c.icon}</div><h3>${c.name}</h3><p>${c.desc}</p><span class="catmeta">${countCat(c.id)} 条</span></article>`).join('');
 const facts=[['完成 enrolment 后再生成课表','选课未完成时，课表可能为空或不完整。','timetable-1'],['抵达澳洲后更新个人信息','住址、联系方式、USI 和 onshore 状态要及时检查。','arrival-1'],['课程期间工作上限','最终以 VEVO 和签证 grant letter 为准。','visa-1'],['Simple Extension','只适用于规定范围，并有申请时间窗口。','assessment-2'],['国际学生交通优惠','多数普通国际学生不自动具备 NSW tertiary concession。','transport-1'],['USU 基础会员免费','可使用社团及多项学生福利。','benefits-1']];
 $('#facts').innerHTML=facts.map(f=>`<div class="fact" data-topic="${f[2]}"><b>${f[0]}</b><span>${f[1]}</span></div>`).join('')
}
function topicCard(t){const c=catMap[t.category],detail=(t.sections||[]).length,kinds=evidenceKinds(t);return `<article class="topic ${detail?'official-detail':''}" data-topic="${t.id}"><div class="top"><span class="type">${t.type==='faq'?'FAQ':t.type==='checklist'?'CHECK':detail?'DETAILED GUIDE':'GUIDE'} · ${c.name}</span><button class="fav ${state.favorites.has(t.id)?'on':''}" data-fav="${t.id}" aria-label="收藏">★</button></div><h3>${esc(t.title)}</h3><p>${esc(t.summary)}</p><div class="topicfoot"><span>${kinds.map(evidenceChip).join(' ')}</span><span>${t.verified||''}</span></div></article>`}
function renderSources(){
 const view=document.querySelector('#sourcesView'),grid=document.querySelector('#sourceGrid');
 if(view&&!document.querySelector('#sourceLegendPage'))grid?.insertAdjacentHTML('beforebegin','<div id="sourceLegendPage"></div>');
 const legend=document.querySelector('#sourceLegendPage');if(legend)legend.innerHTML=evidenceLegend();
 const arr=Object.entries(DATA.sources);if(grid)grid.innerHTML=arr.map(([k,s])=>`<a class="sourcecard" href="${s.url}" target="_blank" rel="noopener"><b>${esc(s.name)}</b><span>${esc(s.authority)} · 核验 ${s.checked}</span><i class="source-kind">查看原文 ↗</i></a>`).join('')
}
function sourceLinks(t){return (t.sourceKeys||[t.source]).map(k=>{const s=DATA.sources[k];return s?`<a class="source-link" href="${s.url}" target="_blank" rel="noopener"><span><b>${esc(s.name)}</b><br><small>${esc(s.authority)} · 核验 ${s.checked}</small></span><b>打开 ↗</b></a>`:''}).join('')}
function articleSection(title,items,ordered=false,cls='',kind='official'){if(!items||!items.length)return'';const tag=ordered?'ol':'ul';return `<section class="article-section ${cls}"><h2><span>${esc(title)}</span><span class="section-source">${esc(DATA.provenancePolicy[kind]?.label||'资料整理')}</span></h2><${tag}>${items.map(x=>`<li>${esc(x)}</li>`).join('')}</${tag}></section>`}
function openTopic(id){const t=topicMap[id];if(!t)return;const c=catMap[t.category],primary=DATA.sources[t.source],detail=(t.sections||[]).length,kinds=evidenceKinds(t);let body=`<div class="eyebrow">${c.name} · ${t.type==='faq'?'常见问题':t.type==='checklist'?'清单项':detail?'详细操作流程':'操作指南'}</div><h1>${esc(t.title)}</h1><p class="summary">${esc(t.summary)}</p><div class="article-source-note">${kinds.map(evidenceChip).join(' ')}</div><div class="article-provenance"><div><b>核验日期</b><span>${t.verified}</span></div><div><b>主要来源</b><span>${esc(primary?.authority||primary?.type||'资料来源')}</span></div></div>`;
 if(t.officialPath)body+=`<div class="official-path"><b>系统路径</b><br>${esc(t.officialPath)}</div>`;
 body+=articleSection('开始前准备',t.prerequisites,false,'','official');
 if(detail){for(const section of t.sections)body+=articleSection(section.title,section.items,true,'',section.sourceKind||'official')}else body+=articleSection('操作要点',t.steps,true,'','official');
 body+=articleSection('注意事项',t.warnings,false,'warning-list','official');
 body+=articleSection('遇到问题',t.troubleshooting,false,'','editorial');
 if(t.communityNotes?.length)body+=`<section class="experience-box"><h2>${evidenceChip('community')} 学生经验</h2><ul>${t.communityNotes.map(x=>`<li>${esc(x)}</li>`).join('')}</ul></section>`;
 if(t.editorNotes?.length)body+=`<section class="editor-box"><h2>${evidenceChip('editorial')} 实操建议</h2><ul>${t.editorNotes.map(x=>`<li>${esc(x)}</li>`).join('')}</ul></section>`;
 body+=`<section class="sourcebox article-section"><h2><span>原始资料</span><span class="section-source">可选</span></h2><details><summary>查看原始页面</summary><div class="source-links">${sourceLinks(t)}</div></details><p style="color:var(--muted);font-size:12px">个人 Offer、学校邮件、Sydney Student、Canvas、签证文件和最新通知优先。</p></section>`;
 $('#drawerBody').innerHTML=body;$('#drawerBack').classList.add('open');$('#drawer').classList.add('open');document.body.style.overflow='hidden';history.replaceState(null,'',`#article=${id}`)
}


(function applySourceLabelUI(){
  const cardCategory=DATA.categories.find(c=>c.id==='card');
  if(cardCategory){cardCategory.name='学生证与校园卡';cardCategory.desc='数字学生证、实体卡、门禁、打印、SydPay 和考试证件。'}
  const search=document.querySelector('#heroSearch');
  if(search) search.placeholder='你现在要解决什么？例如：怎么选课、课表在哪、如何登录 Canvas';
  const popular=document.querySelector('.popular');
  if(popular) popular.innerHTML='<span>常用：</span><button data-query="My Studies">My Studies</button><button data-query="选课">选课</button><button data-query="课表">课表</button><button data-query="Canvas">Canvas</button><button data-query="OSHC">OSHC</button>';
  const sourceButton=[...document.querySelectorAll('[data-go="sources"]')].find(el=>el.closest('.hero'));
  if(sourceButton) sourceButton.textContent='来源说明';
  const sourcesView=document.querySelector('#sourcesView');
  if(sourcesView){
    const h=sourcesView.querySelector('.pagehead h1');
    const p=sourcesView.querySelector('.pagehead p');
    if(h) h.textContent='来源说明';
    if(p) p.textContent='区分官方规定、系统路径、学生经验和实操整理。';
  }
  renderHome();
  renderTopics();
  renderBenefits();
  renderSources();
  const hash=new URLSearchParams(location.hash.replace(/^#/,''));
  if(hash.get('article')) openTopic(hash.get('article'));
})();
