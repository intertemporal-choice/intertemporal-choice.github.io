#!/bin/sh

cd /Volumes/Data/Courses/Choice/LectureNotes/Consumption/Handouts/Equiprobable/Code/Mathematica

rpl -x'.nb' '[Theta]'          '[Theta]1' *
rpl -x'.nb' '[CapitalTheta]'   '[CapitalTheta]1' *
rpl -x'.nb' '[Chi]'            '[Theta]2' *
rpl -x'.nb' '[CapitalChi]'     '[CapitalTheta]2' *
rpl -x'.nb' '[Epislon]'            '[Theta]2' *
rpl -x'.nb' '[CapitalEpislon]'     '[CapitalTheta]2' *
rpl -x'.nb' '[GothicR]' '[ScriptR]' *
rpl -x'.nb' '[Min]'     '[Min]Plot' *
rpl -x'.nb' '[Max]'     '[Max]Plot' *
