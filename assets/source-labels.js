// Provenance policy and selected deep-dive enrichments.
DATA.provenancePolicy={
 official:{label:'官方事实',desc:'直接来自 USYD、CET、澳大利亚政府或 NSW 政府公开页面；用于资格、规则、日期和明确步骤。'},
 system:{label:'官方系统路径',desc:'把官方页面中的按钮、菜单和系统顺序整理成可照做的中文路径；仍以登录后实际界面为准。'},
 community:{label:'学生经验',desc:'来自学生社区、社团或多名使用者的一致反馈，只用于补充实际体验，绝不覆盖官方规则。'},
 editorial:{label:'编辑整理',desc:'本站根据官方信息做出的排查顺序、准备清单和风险提醒；属于实操建议，不冒充学校规定。'}
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
  card.summary='在本站完成从准备、下载、登录、添加到 Apple Wallet、等待权限同步、丢失停用与恢复的完整流程；原始官网仅作为可选核验。';
  card.prerequisites=[
   '你已经完成 enrolment，并能正常使用 UniKey 登录学校系统。',
   '你已经设置校园 Wi‑Fi credentials 与 Okta 多重验证；建议同时准备一个备用验证方式。',
   '学生证照片已经提交并获批。悉尼大学说明照片通常在 3 个工作日内完成审核。',
   'iPhone 已登录个人 Apple ID，系统和 Transact eAccounts 均已更新到当前可用版本。',
   '如计划同时添加 Apple Watch，先确认手表已与这台 iPhone 正常配对。'
  ];
  card.sections=[
   {title:'第一步：安装并连接学校',sourceKind:'official',items:[
    '在 App Store 下载 Transact eAccounts Mobile。',
    '打开应用，划过启动页面后选择 Get Started。',
    '搜索 University of Sydney，并确认选择的是悉尼大学。',
    '使用 UniKey 登录；完成 Okta 验证时，可在 Okta 与 eAccounts 两个应用之间切换。'
   ]},
   {title:'第二步：加入 iPhone 的 Apple Wallet',sourceKind:'official',items:[
    '回到 eAccounts 首页，选择 Add to Apple Wallet。',
    '选择 iPhone，按顺序点击 Next，并同意 Terms & Conditions。',
    '看到凭证添加成功的系统通知后，点击 Done 返回应用。',
    '打开 Apple Wallet，确认 University of Sydney 学生证已经显示。'
   ]},
   {title:'第三步：同时加入 Apple Watch',sourceKind:'official',items:[
    '先确保 iPhone 版本已经成功添加。',
    '返回 eAccounts，再次选择添加凭证，这次选择 Apple Watch。',
    '完成确认流程后，在手表 Wallet 中检查学生证。',
    '官方允许同一学生证加入 1 台 iPhone 和 1 块 Apple Watch。'
   ]},
   {title:'第四步：不要立刻判断“坏了”',sourceKind:'official',items:[
    '建筑门禁和图书馆权限通常在激活后 24 小时内可用。',
    '打印权限通常需要 12–24 小时。',
    '符合资格的 NSW 交通 concession 证明通常需要 2 个工作日；是否符合资格是另一套规则。',
    '不同功能由不同系统同步，所以门禁能用、打印暂时不能用并不矛盾。'
   ]},
   {title:'第五步：实际可使用的场景',sourceKind:'official',items:[
    '进入有权限的校园建筑和部分 24 小时学习空间。',
    '进入图书馆、借书、打印和复印。',
    '使用 SydPay 支付学校打印、复印和部分住宿洗衣服务。',
    '使用校园笔记本电脑自动借用柜等支持学生证的设施。'
   ]},
   {title:'第六步：手机丢失或被盗时',sourceKind:'system',items:[
    '打开 Transact eAccounts，点击右上角 Settings。',
    '进入 Card Management，选择需要停用的 iPhone 或 Apple Watch 凭证并关闭。',
    '也可进入 SydPay 网页端：Card Services → Deactivate Card → 选择具体凭证。',
    '只停用你选择的凭证；没有选择的实体卡、手机或手表版本会继续有效。',
    '无法自行操作时，联系 Student Centre，并明确说明要停用实体卡、手机还是手表。'
   ]},
   {title:'第七步：找回设备后的恢复',sourceKind:'system',items:[
    '在 eAccounts 的 Settings → Card Management 中重新打开相应凭证。',
    '或在 SydPay 网页端选择 Card Services → Activate Card。',
    '等待确认邮件，再测试 Wallet、门禁和打印功能。'
   ]}
  ];
  card.warnings=[
   '数字学生证是可选服务，添加后实体学生证仍然有效。',
   '数字学生证不能用于校内正式考试和 in-semester test 身份核验；考试仍需实体学生证。',
   '手机没电、损坏或无法调出 Wallet 时，数字卡可能无法出示，因此应保留实体卡作为备用。',
   '不要把交通 concession 与普通学生折扣混为一谈；是否有 NSW 交通优惠必须单独确认资格。',
   '学生证只能本人使用，不得转借、截图伪造或以任何方式篡改。'
  ];
  card.troubleshooting=[
   '搜索不到 University of Sydney：先更新 eAccounts，彻底关闭应用后重新打开，再重新搜索。',
   '看不到 Add to Apple Wallet：依次确认 enrolment、照片审批、UniKey、Okta 和设备兼容性。',
   'Okta 完成后又回到登录页：先回到 eAccounts 等待几秒；仍失败再退出重登，不要连续重复添加凭证。',
   'Wallet 已有学生证但门禁无效：先等待官方同步时限；记录建筑、时间、是否有提示音，再联系 Student Centre 或相关门禁支持。',
   '打印不能用：先确认 SydPay 已建立、余额和打印账户正常，并等待 12–24 小时同步。',
   '联系支持前准备：报错截图、发生时间、设备型号、iOS 版本、eAccounts 版本、照片是否已获批。'
  ];
  card.editorNotes=[
   '先确认“资格是否具备”，再排查“App 是否正常”，最后才是“门禁/打印权限是否同步”，可以避免反复卸载和重复注册。',
   '对任何外部攻略里的等待时间、交通优惠和考试用途，都应回到本页的官方事实标签核对。'
  ];
 }
 const lost=byId['card-8'];
 if(lost){
  lost.officialPath='eAccounts → Settings → Card Management → 选择设备凭证 → 关闭；或 SydPay → Card Services → Deactivate Card';
  lost.prerequisites=['确认丢失的是实体卡、iPhone、Apple Watch，还是不止一种。','尽可能先使用 Find My 锁定 Apple 设备。'];
  lost.sections=[
   {title:'通过 eAccounts 停用',sourceKind:'system',items:['进入 Settings。','选择 Card Management。','选择丢失设备对应的 credential 并关闭。','检查确认邮件。']},
   {title:'通过 SydPay 网页端停用',sourceKind:'system',items:['进入 Card Services。','选择 Deactivate Card。','选择具体 credential 并确认。','检查确认邮件。']},
   {title:'找回后恢复',sourceKind:'system',items:['回到 Card Management 或 SydPay 的 Activate Card。','只重新启用已找回且安全的设备凭证。','重新测试门禁、图书馆和打印。']}
  ];
  lost.warnings=['停用时必须说明具体凭证；未选择的实体卡、手机或手表会保持有效。','若涉及 SydPay 异常消费或门禁事件，应分别联系 ICT/Shared Service Centre 或 Campus Assist。'];
  lost.editorNotes=['停卡后保留确认邮件、报失时间和 case number，后续发生争议时更容易说明。'];
 }
})();

function evidenceChip(kind){const p=DATA.provenancePolicy[kind];return p?`<span class="evidence-chip ${kind}">${esc(p.label)}</span>`:''}
function evidenceKinds(t){const explicit=DATA.topicEvidence[t.id]||{};const kinds=[];if((t.sourceKeys||[t.source]).some(k=>DATA.sources[k]?.firstParty))kinds.push('official');if(t.officialPath||(t.sections||[]).some(s=>s.sourceKind==='system'))kinds.push('system');if(t.communityNotes?.length||explicit.community)kinds.push('community');if(t.editorNotes?.length||t.troubleshooting?.length||explicit.editorial)kinds.push('editorial');return [...new Set(kinds)]}
function evidenceLegend(compact=false){const p=DATA.provenancePolicy;return `<section class="evidence-legend"><h2>${compact?'怎么看资料标注':'内容留在本站，来源清楚标注'}</h2><p>你不需要跳到别的网站才能读懂。正文已经把信息完整整理在本页；外部链接只放在文末，供你在时间敏感、个人情况或需要核对原文时选择打开。</p><div class="evidence-grid">${Object.entries(p).map(([k,v])=>`<div class="evidence-item ${k}">${evidenceChip(k)}<b>${esc(v.label)}</b><p>${esc(v.desc)}</p></div>`).join('')}</div></section>`}
function renderHome(){
 const guides=DATA.topics.filter(t=>t.type==='guide').length,faqs=DATA.topics.filter(t=>t.type==='faq').length;
 $('#stats').innerHTML=[[DATA.topics.length,'可搜索条目'],[DATA.editorialGuideCount,'深度操作流程'],[faqs,'常见问题'],[Object.keys(DATA.sources).length,'已核验原始来源']].map(x=>`<div class="stat"><b>${x[0]}</b><span>${x[1]}</span></div>`).join('');
 const hero=document.querySelector('#homeView .hero');if(hero&&!document.querySelector('#homeEvidenceLegend'))hero.insertAdjacentHTML('afterend',`<div id="homeEvidenceLegend">${evidenceLegend()}</div>`);
 $('#homeCategories').innerHTML=DATA.categories.map(c=>`<article class="catcard" data-cat="${c.id}"><div class="caticon">${c.icon}</div><h3>${c.name}</h3><p>${c.desc}</p><span class="catmeta">${countCat(c.id)} 条</span></article>`).join('');
 const facts=[['数字学生证可加入 Apple Wallet','完整步骤、等待时间、停用与恢复都在本站内。','card-1'],['DEC 15 第二个 2026 intake','个人日期仍以 offer 为准。','cet-1'],['课程期间工作上限','最终以 VEVO 和 grant letter 为准。','visa-1'],['Simple Extension','有适用范围和申请窗口。','assessment-2'],['国际学生交通优惠','多数普通国际学生不自动具备 NSW tertiary concession。','transport-1'],['USU 基础会员免费','可使用社团及多项学生福利。','benefits-1']];
 $('#facts').innerHTML=facts.map(f=>`<div class="fact" data-topic="${f[2]}"><b>${f[0]}</b><span>${f[1]}</span></div>`).join('')
}
function topicCard(t){const c=catMap[t.category],detail=(t.sections||[]).length,kinds=evidenceKinds(t);return `<article class="topic ${detail?'official-detail':''}" data-topic="${t.id}"><div class="top"><span class="type">${t.type==='faq'?'FAQ':t.type==='checklist'?'CHECK':detail?'DETAILED GUIDE':'GUIDE'} · ${c.name}</span><button class="fav ${state.favorites.has(t.id)?'on':''}" data-fav="${t.id}" aria-label="收藏">★</button></div><h3>${esc(t.title)}</h3><p>${esc(t.summary)}</p><div class="topicfoot"><span>${kinds.map(evidenceChip).join(' ')}</span><span>正文内阅读</span></div></article>`}
function renderSources(){
 $('#sourceLegendPage').innerHTML=evidenceLegend(true)+`<div class="provenance-policy"><b>采用原则：</b>官方来源决定规则与资格；官方系统路径解释怎样操作；学生经验只补充“实际会遇到什么”，必须清楚标注且不能覆盖官方规则；编辑整理只负责把多个页面变成可执行顺序。外部原文不会取代本站正文。</div>`;
 const arr=Object.entries(DATA.sources);$('#sourceGrid').innerHTML=arr.map(([k,s])=>`<a class="sourcecard" href="${s.url}" target="_blank" rel="noopener"><b>${esc(s.name)}</b><span>${esc(s.authority)} · 原始页面 · 核验 ${s.checked}</span><i class="source-kind">可选核验 ↗</i></a>`).join('')
}
function sourceLinks(t){return (t.sourceKeys||[t.source]).map(k=>{const s=DATA.sources[k];return s?`<a class="source-link" href="${s.url}" target="_blank" rel="noopener"><span><b>${esc(s.name)}</b><br><small>${esc(s.authority)} · 原始页面 · 核验 ${s.checked}</small></span><b>核验 ↗</b></a>`:''}).join('')}
function articleSection(title,items,ordered=false,cls='',kind='official'){if(!items||!items.length)return'';const tag=ordered?'ol':'ul';return `<section class="article-section ${cls}"><h2><span>${esc(title)}</span><span class="section-source">${esc(DATA.provenancePolicy[kind]?.label||'资料整理')}</span></h2><${tag}>${items.map(x=>`<li>${esc(x)}</li>`).join('')}</${tag}></section>`}
function openTopic(id){const t=topicMap[id];if(!t)return;const c=catMap[t.category],primary=DATA.sources[t.source],detail=(t.sections||[]).length,kinds=evidenceKinds(t);let body=`<div class="eyebrow">${c.name} · ${t.type==='faq'?'常见问题':t.type==='checklist'?'清单项':detail?'详细操作流程':'操作指南'}</div><h1>${esc(t.title)}</h1><p class="summary">${esc(t.summary)}</p><div class="article-source-note">${kinds.map(evidenceChip).join('')}<span>正文已在本站完整整理；标签说明每部分依据，不要求外跳阅读。</span></div><div class="article-provenance"><div><b>内容方式</b><span>本页内完整阅读</span></div><div><b>最后核验</b><span>${t.verified}</span></div><div><b>主要机构</b><span>${esc(primary?.authority||primary?.type||'资料来源')}</span></div></div>`;
 if(t.officialPath)body+=`<div class="official-path"><b>官方系统路径</b><br>${esc(t.officialPath)}</div>`;
 body+=articleSection('开始前准备',t.prerequisites,false,'','official');
 if(detail){for(const section of t.sections)body+=articleSection(section.title,section.items,true,'',section.sourceKind||'official')}else body+=articleSection('建议操作顺序',t.steps,true,'','official');
 body+=articleSection('必须注意',t.warnings,false,'warning-list','official');
 body+=articleSection('失败时这样排查',t.troubleshooting,false,'','editorial');
 if(t.communityNotes?.length)body+=`<section class="experience-box"><h2>${evidenceChip('community')} 学生经验补充</h2><p>只用于补充实际体验，不作为学校规则。</p><ul>${t.communityNotes.map(x=>`<li>${esc(x)}</li>`).join('')}</ul></section>`;
 if(t.editorNotes?.length)body+=`<section class="editor-box"><h2>${evidenceChip('editorial')} 编辑实操建议</h2><p>根据官方页面整理出的执行顺序和排查建议。</p><ul>${t.editorNotes.map(x=>`<li>${esc(x)}</li>`).join('')}</ul></section>`;
 body+=`<section class="sourcebox article-section"><h2><span>资料依据</span><span class="section-source">可选核验</span></h2><p style="color:var(--muted);font-size:13px;line-height:1.7">你已经在本页读到完整内容。下面的链接只用于核对最新原文、个人资格或学校页面变化，不是阅读正文的必经步骤。</p><details><summary>展开原始页面链接</summary><div class="source-links">${sourceLinks(t)}</div></details><p style="color:var(--muted);font-size:12px">个人 Offer、学校邮件、Sydney Student、Canvas、签证文件和最新官方通知始终优先。</p></section>`;
 $('#drawerBody').innerHTML=body;$('#drawerBack').classList.add('open');$('#drawer').classList.add('open');document.body.style.overflow='hidden';history.replaceState(null,'',`#article=${id}`)
}

(function applySourceLabelUI(){
  const sourceButton=[...document.querySelectorAll('[data-go="sources"]')].find(el=>el.closest('.hero'));
  if(sourceButton) sourceButton.textContent='了解资料标注';
  const sourcesView=document.querySelector('#sourcesView');
  if(sourcesView){
    const h=sourcesView.querySelector('.pagehead h1');
    const p=sourcesView.querySelector('.pagehead p');
    if(h) h.textContent='资料来源与可信度';
    if(p) p.textContent='正文全部留在本站阅读；这里解释标注规则，并提供可选的原始页面核验入口。';
  }
  renderHome();
  renderTopics();
  renderBenefits();
  renderSources();
  const hash=new URLSearchParams(location.hash.replace(/^#/,''));
  if(hash.get('article')) openTopic(hash.get('article'));
})();
